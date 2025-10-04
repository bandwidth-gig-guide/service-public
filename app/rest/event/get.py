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
            Event.OriginalPostUrl,
            Event.TicketSaleUrl,
            Event.IsFeatured,
            
            (
                SELECT json_agg(
                    Image.Url 
                    ORDER BY 
                        ImageGroup.priority, 
                        ImageGroup.artist_position, 
                        ImageGroup.image_position
                )
                FROM (
                    SELECT 
                        EventImage.ImageID,
                        1 AS priority,
                        NULL AS artist_position,
                        EventImage.DisplayOrder AS image_position
                    FROM EventImage
                    WHERE EventImage.EventID = Event.EventID

                    UNION ALL

                    SELECT 
                        ArtistImage.ImageID,
                        2 AS priority,
                        EventPerformance.SetListPosition AS artist_position,
                        ArtistImage.DisplayOrder AS image_position
                    FROM ArtistImage
                    JOIN EventPerformance ON ArtistImage.ArtistID = EventPerformance.ArtistID
                    WHERE EventPerformance.EventID = Event.EventID

                    UNION ALL

                    SELECT 
                        VenueImage.ImageID,
                        3 AS priority,
                        NULL AS artist_position,
                        VenueImage.DisplayOrder AS image_position
                    FROM VenueImage
                    WHERE VenueImage.VenueID = Event.VenueID
                    
                ) AS ImageGroup
                JOIN Image ON Image.ImageID = ImageGroup.ImageID
            ) AS ImageUrls,

            (
                SELECT json_agg(json_build_object(
                    'SocialPlatform', SocialPlatform,
                    'Handle', Handle,
                    'Url', Url
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
                    'ImageUrl', (
                        SELECT Image.Url
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
                        'ImageUrl', (
                            SELECT Image.Url
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