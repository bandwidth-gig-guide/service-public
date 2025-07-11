from pydantic import BaseModel, HttpUrl
from typing import Optional, List
from uuid import UUID
from app.model.social import Social
from app.model.opening_hours import OpeningHours as Hours

class VenueComplete(BaseModel):
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
    ImageURLs: Optional[List[str]] = None
    Socials: Optional[List[Social]] = None
    Types: Optional[List[str]] = None
    Tags: Optional[List[str]] = None
    OpeningHours: Optional[Hours] = None