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
    WebsiteUrl: HttpUrl
    PhoneNumber: str
    GoogleMapsEmbedUrl: Optional[HttpUrl] = None
    IsFeatured: bool
    IsMonitored: bool
    ImageUrls: Optional[List[HttpUrl]] = None
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
        WebsiteUrl = tuple[7],
        PhoneNumber = tuple[8],
        GoogleMapsEmbedUrl = tuple[9],
        IsFeatured = tuple[10],
        IsMonitored = tuple[11],
        ImageUrls = tuple[12] or [],
        Socials = tuple[13] or [],
        Types = tuple[14] or [],
        Tags = tuple[15] or [],
        OpeningHours = tuple[16],
        UpcomingEventIDs = tuple[17] or []
    )