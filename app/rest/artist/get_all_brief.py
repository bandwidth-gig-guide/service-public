from app.query.fetch_list import execute
from app.model.artist_brief import ArtistBrief, format

def get_all_brief() -> list[ArtistBrief]:
    rows = execute(query())
    return [format(row) for row in rows]

def query():
    return """
        SELECT 
            Artist.ArtistID,
            Artist.Title,
            Artist.Country,
            Artist.City,
            Artist.IsFeatured,

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
                WHERE ArtistID = Artist.ArtistID 
                AND StartDateTime > NOW()
            ) AS EventCount

        FROM Artist
        ORDER BY Artist.IsFeatured DESC, Artist.Title ASC;
    """
