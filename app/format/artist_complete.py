from app.model.artist_complete import ArtistComplete

def format(tuple: tuple) -> ArtistComplete:

    return ArtistComplete (
        ArtistID = tuple[0],
        Title = tuple[1],
        Country = tuple[2],
        City = tuple[3],
        StateCode = tuple[4],
        YearFounded = tuple[5],
        Description = tuple[6],
        SpotifyEmbedURL = tuple[7],
        YoutubeEmbedURL = tuple[8],
        IsFeatured = tuple[9],
        Images = tuple[10] or [],
        Socials = tuple[11] or [],
        Types = tuple[12] or [],
        Tags = tuple[13] or []
    )
