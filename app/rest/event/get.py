from app.query.fetch_one import execute
from app.model.event import Event, format
from uuid import UUID

def get_complete(event_id: UUID) -> Event:
    response = execute(query(), value(event_id))
    return format(response)

def query():
    return """
        SELECT 
            Event.EventID,
            Event.Title,
            Event.StartDateTime,
            Event.Description,
            Event.OriginalPostURL,
            Event.TicketSaleURL,

            EXISTS(
                SELECT 1 
                FROM EventFeatured 
                WHERE EventID = Event.EventID
            ) AS isFeatured,

            (
                SELECT json_agg(
                    Image.URL 
                    ORDER BY EventImage.DisplayOrder ASC
                )
                FROM Image
                JOIN EventImage ON Image.ImageID = EventImage.ImageID
                WHERE EventImage.EventID = Event.EventID
            ) AS ImageURLs,

            (
                SELECT json_agg(json_build_object(
                    'SocialPlatform', SocialPlatform,
                    'Handle', Handle,
                    'URL', URL
                ))
                FROM EventSocial
                WHERE EventSocial.EventID = Event.EventID
            ) AS Socials,

            (
                SELECT json_agg(Type)
                FROM EventType
                WHERE EventType.EventID = Event.EventID
            ) AS Types,

            (
                SELECT json_agg(Tag)
                FROM EventTag
                WHERE EventTag.EventID = Event.EventID
            ) AS Tags,

            (
                SELECT json_build_object(
                    'VenueID', Venue.VenueID,
                    'Title', Venue.Title,
                    'StageTitle', VenueStage.Title,
                    'ImageURL', (
                        SELECT Image.URL
                        FROM VenueImage
                        JOIN Image ON Image.ImageID = VenueImage.ImageID
                        WHERE VenueImage.VenueID = Venue.VenueID
                        ORDER BY VenueImage.DisplayOrder ASC
                        LIMIT 1
                    )
                )
                FROM Venue
                JOIN VenueStage ON VenueStage.StageID = Event.StageID
                WHERE Venue.VenueID = Event.VenueID
                LIMIT 1
            ) AS Venue,

            (
                SELECT json_agg(
                    json_build_object(
                        'ArtistID', EventPerformance.ArtistID,
                        'Title', Artist.Title,
                        'ImageURL', (
                            SELECT Image.URL
                            FROM ArtistImage
                            JOIN Image ON Image.ImageID = ArtistImage.ImageID
                            WHERE ArtistImage.ArtistID = Artist.ArtistID
                            ORDER BY ArtistImage.DisplayOrder ASC
                            LIMIT 1
                        ),
                        'SetListPosition', EventPerformance.SetListPosition,
                        'StartDateTime', EventPerformance.StartDateTime
                    )
                    ORDER BY EventPerformance.SetListPosition
                )
                FROM EventPerformance
                JOIN Artist ON Artist.ArtistID = EventPerformance.ArtistID
                WHERE EventPerformance.EventID = Event.EventID
            ) AS Performances,
                
            (
                SELECT json_agg(json_build_object(
                    'TicketType', TicketType,
                    'Price', Price
                ))
                FROM EventPrice
                WHERE EventPrice.EventID = Event.EventID
            ) AS Prices

        FROM Event
        WHERE Event.EventID = %s;
    """

def value(event_id: UUID):
    return (str(event_id),)