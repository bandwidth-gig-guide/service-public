from uuid import UUID
from app.query.fetch_list import execute

def get_recommended(artist_id: UUID) -> list[UUID]:
    rows = execute(query(), value(artist_id))
    return [row[0] for row in rows]

def query():
    return """
        WITH SimilarArtists AS (
            SELECT Artist.ArtistID
            FROM Artist
            JOIN ArtistTag ON Artist.ArtistID = ArtistTag.ArtistID
            WHERE Artist.ArtistID != %s
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
                AND Artist.ArtistID NOT IN (SELECT ArtistID FROM SimilarArtists)
                ORDER BY RANDOM()
                LIMIT 4
            )
        )
        ORDER BY RANDOM()
        LIMIT 8;
    """

def value(artist_id: UUID):
    return (str(artist_id), str(artist_id), str(artist_id))