from app.query.fetch_one import execute
from app.model.artist import Artist, format
from uuid import UUID

def get_complete(artist_id: UUID) -> Artist:
    response = execute(query(), value(artist_id))
    return format(response)

def query():
    return """
        SELECT 
            Artist.ArtistID,
            Artist.Title,
            Artist.Country,
            Artist.City,
            Artist.StateCode,
            Artist.YearFounded,
            Artist.Description,
            Artist.SpotifyEmbedUrl,
            Artist.YoutubeEmbedUrl,
            Artist.IsFeatured,
            Artist.IsResearched,

            (
                SELECT json_agg(Image.Url ORDER BY ArtistImage.DisplayOrder ASC)
                FROM Image
                JOIN ArtistImage ON Image.ImageID = ArtistImage.ImageID
                WHERE ArtistImage.ArtistID = Artist.ArtistID
            ) AS ImageUrls,

            (
                SELECT json_agg(json_build_object(
                    'SocialPlatform', SocialPlatform,
                    'Handle', Handle,
                    'Url', Url
                ))
                FROM ArtistSocial
                WHERE ArtistSocial.ArtistID = Artist.ArtistID
            ) AS Socials,

            (
                SELECT json_agg(Type)
                FROM ArtistType
                WHERE ArtistType.ArtistID = Artist.ArtistID
            ) AS Types,

            (
                SELECT json_agg(Tag)
                FROM ArtistTag
                WHERE ArtistTag.ArtistID = Artist.ArtistID
            ) AS Tags,

            (
                SELECT json_agg(
                    EventID
                    ORDER BY StartDateTime ASC    
                )
                FROM EventPerformance
                WHERE EventPerformance.ArtistID = Artist.ArtistID
                AND EventPerformance.StartDateTime > NOW()
            ) AS UpcomingEventIDs

        FROM Artist
        WHERE Artist.ArtistID = %s;
    """

def value(artist_id: UUID):
    return (str(artist_id),)