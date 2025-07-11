from app.query.fetch_list import execute
from app.model.event_brief import EventBrief, format

def get_all_brief() -> list[EventBrief]:
    rows = execute(query())
    return [format(row) for row in rows]

def query():
    return """
        SELECT 
            Event.EventID,
            Event.Title,
            Event.StartDateTime,

            (
                SELECT Title
                FROM Venue
                WHERE Venue.VenueID = Event.VenueID
            ) AS VenueTitle,

            EXISTS(
                SELECT 1 
                FROM EventFeatured 
                WHERE EventID = Event.EventID
            ) AS IsFeatured,

            (
                SELECT URL 
                FROM Image 
                JOIN EventImage ON Image.ImageID = EventImage.ImageID 
                WHERE EventImage.EventID = Event.EventID 
                ORDER BY DisplayOrder ASC 
                LIMIT 1
            ) AS ImageURL,

            (
                SELECT json_agg(Title ORDER BY SetListPosition ASC)
                FROM Artist
                JOIN EventPerformance ON Artist.ArtistID = EventPerformance.ArtistID
                WHERE EventPerformance.EventID = Event.EventID
            ) AS ArtistTitles,

            (
                SELECT Price
                FROM EventPrice
                WHERE EventPrice.EventID = Event.EventID
                ORDER BY Price ASC
                LIMIT 1
            ) AS MinPrice
            
        FROM Event;
    """
