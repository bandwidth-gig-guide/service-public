from app.model.artist_card import ArtistCard

def format(tuple: tuple) -> ArtistCard:
    return ArtistCard (
        ArtistID = tuple[0],
        Title = tuple[1],
        Country = tuple[2],
        City = tuple[3],
        IsFeatured = tuple[4],
        ImageURL = tuple[5],
        UpcomingEvents = tuple[6]
    )