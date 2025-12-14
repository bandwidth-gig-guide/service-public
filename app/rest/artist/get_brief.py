from app.query.fetch_one import execute
from app.model.artist_brief import ArtistBrief, format
from uuid import UUID

def get_brief(artist_id: UUID) -> ArtistBrief:
    response = execute(query(), values(artist_id))
    return format(response)

def query():
    return """
        SELECT 
            Artist.ArtistID,
            Artist.Title,
            Artist.Country,
            Artist.City,
            Artist.IsFeatured,
            Artist.IsResearched,

            (
                SELECT Url 
                FROM Image 
                JOIN ArtistImage ON Image.ImageID = ArtistImage.ImageID 
                WHERE ArtistImage.ArtistID = Artist.ArtistID 
                ORDER BY DisplayOrder ASC 
                LIMIT 1
            ) AS ImageUrl,

            (
                SELECT COUNT(*) 
                FROM EventPerformance 
                WHERE ArtistID = Artist.ArtistID AND StartDateTime > NOW()
            ) AS EventCount
            
        FROM Artist 
        WHERE ArtistID = %s;
    """

def values(artist_id: UUID):
    return (str(artist_id),)