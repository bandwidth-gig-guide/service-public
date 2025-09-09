from app.query.fetch_one import execute
from app.model.venue_brief import VenueBrief, format
from uuid import UUID

def get_brief(venue_id: UUID) -> VenueBrief:
    response = execute(query(), values(venue_id))
    return format(response)

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
                SELECT Url 
                FROM Image 
                JOIN VenueImage ON Image.ImageID = VenueImage.ImageID 
                WHERE VenueImage.VenueID = Venue.VenueID 
                ORDER BY DisplayOrder ASC 
                LIMIT 1
            ) AS ImageUrl,

            (
                SELECT COUNT(DISTINCT EventID) 
                FROM EventPerformance 
                WHERE VenueID = Venue.VenueID AND StartDateTime > NOW()
            ) AS UpcomingEventCount

        FROM Venue 
        WHERE VenueID = %s;
    """

def values(venue_id: UUID):
    return (str(venue_id),)
