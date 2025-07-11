from app.query.fetch_one import execute
from app.format.venue_card import format
from app.model.venue_card import VenueCard
from uuid import UUID

def get(venue_id: UUID) -> VenueCard:
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
                WHERE VenueID = %s
            ) AS IsFeatured,
            (
                SELECT URL 
                FROM Image 
                JOIN VenueImage ON Image.ImageID = VenueImage.ImageID 
                WHERE VenueImage.VenueID = %s 
                ORDER BY DisplayOrder ASC 
                LIMIT 1
            ) AS ImageURL,
            (
                SELECT COUNT(*) 
                FROM EventPerformance 
                WHERE VenueID = %s AND StartDateTime > NOW()
            ) AS UpcomingEventCount
        FROM Venue 
        WHERE VenueID = %s;
    """

def values(venue_id: UUID):
    return (
        str(venue_id),
        str(venue_id),
        str(venue_id),
        str(venue_id)
    )