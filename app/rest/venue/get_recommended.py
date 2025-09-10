from uuid import UUID
from app.query.fetch_list import execute

def get_recommended(venue_id: UUID) -> list[UUID]:
    rows = execute(query(), value(venue_id))
    return [row[0] for row in rows]

def query():
    return """
        WITH SimilarVenues AS (
            SELECT Venue.VenueID
            FROM Venue
            JOIN VenueTag ON Venue.VenueID = VenueTag.VenueID
            WHERE Venue.VenueID != %s
            AND VenueTag.Tag IN 
            (
                SELECT Tag 
                FROM VenueTag 
                WHERE VenueID = %s
            )
            GROUP BY Venue.VenueID
            ORDER BY COUNT(*) DESC, RANDOM()
            LIMIT 10
        )

        SELECT VenueID
        FROM 
        (
            (
                SELECT VenueID
                FROM SimilarVenues
            )
            UNION
            (
                SELECT Venue.VenueID
                FROM Venue
                JOIN VenueFeatured ON Venue.VenueID = VenueFeatured.VenueID
                WHERE Venue.VenueID != %s
                AND Venue.VenueID NOT IN (SELECT VenueID FROM SimilarVenues)
                ORDER BY RANDOM()
                LIMIT 2
            )
        )
        ORDER BY RANDOM()
        LIMIT 8;
    """

def value(venue_id: UUID):
    return (str(venue_id), str(venue_id), str(venue_id))