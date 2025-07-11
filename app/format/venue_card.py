from app.model.venue_card import VenueCard

def format(tuple: tuple) -> VenueCard:
    return VenueCard (
        VenueID = tuple[0],
        Title = tuple[1],
        City = tuple[2],
        StreetAddress = tuple[3],
        StateCode = tuple[4],
        PostCode = tuple[5],
        IsFeatured = tuple[6],
        ImageURL = tuple[7],
        UpcomingEventCount = tuple[8]
    )