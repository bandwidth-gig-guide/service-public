from app.model.venue_complete import VenueComplete

def format(tuple: tuple) -> VenueComplete:

    return VenueComplete (
        VenueID = tuple[0],
        Title = tuple[1],
        City = tuple[2],
        StateCode = tuple[3],
        StreetAddress = tuple[4],
        PostCode = tuple[5],
        Description = tuple[6],
        WebsiteURL = tuple[7],
        PhoneNumber = tuple[8],
        GoogleMapsEmbedURL = tuple[9],
        IsFeatured = tuple[10],
        Images = tuple[11] or [],
        Socials = tuple[12] or [],
        Types = tuple[13] or [],
        Tags = tuple[14] or [],
        OpeningHours = tuple[15]
    )
