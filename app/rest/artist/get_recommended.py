from uuid import UUID
from app.query.fetch_list import execute
from app.const.reserved_uuids import RESERVED_UUIDS_STRING


def get_recommended(artist_id: UUID) -> list[UUID]:
    rows = execute(query(), value(artist_id))
    result = [row[0] for row in rows]
    
    if len(result) < 8:
        random_rows = execute(fallback_query(), fallback_value(artist_id))
        result.extend([row[0] for row in random_rows if row[0] not in result])
    
    return result[:8]


def query():
    return """
        WITH SimilarArtists AS (
            SELECT Artist.ArtistID
            FROM Artist
            JOIN ArtistTag ON Artist.ArtistID = ArtistTag.ArtistID
            WHERE Artist.ArtistID != %s
            AND Artist.ArtistID NOT IN ({})
            AND ArtistTag.Tag IN 
            (
                SELECT Tag 
                FROM ArtistTag 
                WHERE ArtistID = %s
            )
            GROUP BY Artist.ArtistID
            ORDER BY COUNT(*) DESC, RANDOM()
            LIMIT 12
        )

        SELECT ArtistID
        FROM 
        (
            (
                SELECT ArtistID
                FROM SimilarArtists
            )
            UNION
            (
                SELECT Artist.ArtistID
                FROM Artist
                WHERE Artist.IsFeatured = TRUE
                AND Artist.ArtistID != %s
                AND Artist.ArtistID NOT IN ({})
                AND Artist.ArtistID NOT IN (SELECT ArtistID FROM SimilarArtists)
                ORDER BY RANDOM()
                LIMIT 4
            )
        )
        ORDER BY RANDOM()
        LIMIT 8;
    """.format(RESERVED_UUIDS_STRING, RESERVED_UUIDS_STRING)

def value(artist_id: UUID):
    return (str(artist_id), str(artist_id), str(artist_id))



def fallback_query():
    return """
        SELECT Artist.ArtistID
        FROM Artist
        WHERE Artist.ArtistID != %s
        ORDER BY RANDOM()
        LIMIT 8;
    """

def fallback_value(artist_id: UUID):
    return (str(artist_id), )
