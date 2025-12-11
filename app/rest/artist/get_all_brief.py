from app.query.fetch_list import execute
from app.model.artist_brief import ArtistBrief, format
from app.const.reserved_uuids import RESERVED_UUIDS_STRING

def get_all_brief() -> list[ArtistBrief]:
    rows = execute(query())
    return [format(row) for row in rows]

def query():
    return f"""
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
        WHERE Artist.ArtistID NOT IN ({RESERVED_UUIDS_STRING})
        ORDER BY Artist.IsFeatured DESC, Artist.Title ASC;
    """
