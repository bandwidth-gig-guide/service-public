from uuid import UUID
from app.query.fetch_list import execute
from app.const.reserved_uuids import RESERVED_UUIDS_STRING

def get_recommended(venue_id: UUID) -> list[UUID]:
    rows = execute(query(), value(venue_id))
    result = [row[0] for row in rows]
    
    if len(result) < 8:
        random_rows = execute(fallback_query(), fallback_value(venue_id))
        result.extend([row[0] for row in random_rows if row[0] not in result])
    
    return result[:8]


def query():
    return """
        WITH SimilarVenues AS (
            SELECT Venue.VenueID
            FROM Venue
            JOIN VenueTag ON Venue.VenueID = VenueTag.VenueID
            WHERE Venue.VenueID != %s
            AND Venue.VenueID NOT IN ({})
            AND VenueTag.Tag IN 
            (
                SELECT Tag 
                FROM VenueTag 
                WHERE VenueID = %s
            )
            GROUP BY Venue.VenueID
            ORDER BY COUNT(*) DESC, RANDOM()
            LIMIT 12
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
                WHERE Venue.IsFeatured = TRUE
                AND Venue.VenueID != %s
                AND Venue.VenueID NOT IN ({})
                AND Venue.VenueID NOT IN (SELECT VenueID FROM SimilarVenues)
                ORDER BY RANDOM()
                LIMIT 4
            )
        )
        ORDER BY RANDOM()
        LIMIT 8;
    """.format(RESERVED_UUIDS_STRING, RESERVED_UUIDS_STRING)

def value(venue_id: UUID):
    return (str(venue_id), str(venue_id), str(venue_id))


def fallback_query():
    return """
        SELECT Venue.VenueID
        FROM Venue
        WHERE Venue.VenueID != %s
        ORDER BY RANDOM()
        LIMIT 8;
    """

def fallback_value(venue_id: UUID):
    return (str(venue_id), )
