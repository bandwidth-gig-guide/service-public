from app.query.fetch_list import execute
from app.format.venue_card import format
from app.model.venue_card import VenueCard

def get_all() -> list[VenueCard]:
    rows = execute(query())
    return [format(row) for row in rows]

def query():
    return """
        SELECT 
            Venue.VenueID,
            Venue.Title,
            Venue.City,
            Venue.StreetAddress,
            Venue.StateCode,
            Venue.PostCode,
            EXISTS(
                SELECT 1 
                FROM VenueFeatured 
                WHERE VenueID = Venue.VenueID
            ) AS IsFeatured,
            (
                SELECT URL 
                FROM Image 
                JOIN VenueImage ON Image.ImageID = VenueImage.ImageID 
                WHERE VenueImage.VenueID = Venue.VenueID 
                ORDER BY DisplayOrder ASC 
                LIMIT 1
            ) AS ImageURL,
            (
                SELECT COUNT(*) 
                FROM EventPerformance 
                WHERE VenueID = Venue.VenueID AND StartDateTime > NOW()
            ) AS EventCount
        FROM Venue;
    """