from pydantic import BaseModel, HttpUrl
from typing import Optional, List
from uuid import UUID
from app.model.social import Social
from app.model.opening_hours import OpeningHours as Hours

class Venue(BaseModel):
    VenueID: UUID
    Title: str
    City: str
    StateCode: str
    StreetAddress: str
    StateCode: str
    PostCode: int
    Description: str
    WebsiteURL: HttpUrl
    PhoneNumber: str
    GoogleMapsEmbedURL: Optional[HttpUrl] = None
    IsFeatured: bool
    ImageURLs: Optional[List[HttpUrl]] = None
    Socials: Optional[List[Social]] = None
    Types: Optional[List[str]] = None
    Tags: Optional[List[str]] = None
    OpeningHours: Optional[Hours] = None
    UpcomingEventIDs: Optional[List[UUID]] = None

def format(tuple: tuple) -> Venue:
    return Venue (
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
        OpeningHours = tuple[15],
        UpcomingEventIDs = tuple[16] or []
    )