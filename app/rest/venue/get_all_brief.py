from app.query.fetch_list import execute
from app.model.venue_brief import VenueBrief, format

def get_all_brief() -> list[VenueBrief]:
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
            Venue.IsFeatured,

            (
                SELECT Url 
                FROM Image 
                JOIN VenueImage ON Image.ImageID = VenueImage.ImageID 
                WHERE VenueImage.VenueID = Venue.VenueID 
                ORDER BY DisplayOrder ASC 
                LIMIT 1
            ) AS ImageUrl,

            (
                SELECT COUNT(DISTINCT EventID) 
                FROM Event 
                WHERE VenueID = Venue.VenueID AND StartDateTime > NOW()
            ) AS EventCount

        FROM Venue
        ORDER BY Venue.IsFeatured DESC, Venue.Title ASC;
    """
