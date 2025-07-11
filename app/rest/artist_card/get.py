from app.query.fetch_one import execute
from app.format.artist_card import format
from app.model.artist_card import ArtistCard
from uuid import UUID

def get(artist_id: UUID) -> ArtistCard:
    response = execute(query(), values(artist_id))
    return format(response)

def query():
    return """
        SELECT 
            Artist.ArtistID,
            Artist.Title,
            Artist.Country,
            Artist.City,
            EXISTS(
                SELECT 1 
                FROM ArtistFeatured 
                WHERE ArtistID = %s
            ) AS IsFeatured,
            (
                SELECT URL 
                FROM Image 
                JOIN ArtistImage ON Image.ImageID = ArtistImage.ImageID 
                WHERE ArtistImage.ArtistID = %s 
                ORDER BY DisplayOrder ASC 
                LIMIT 1
            ) AS ImageURL,
            (
                SELECT COUNT(*) 
                FROM EventPerformance 
                WHERE ArtistID = %s AND StartDateTime > NOW()
            ) AS EventCount
        FROM Artist 
        WHERE ArtistID = %s;
    """

def values(artist_id: UUID):
    return (
        str(artist_id),
        str(artist_id),
        str(artist_id),
        str(artist_id)
    )