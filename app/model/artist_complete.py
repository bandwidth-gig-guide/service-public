from pydantic import BaseModel, HttpUrl
from typing import Optional, List
from uuid import UUID
from app.model.social import Social

class ArtistComplete(BaseModel):
    ArtistID: UUID
    Title: str
    Country: str
    City: str
    StateCode: str
    YearFounded: int
    Description: str
    SpotifyEmbedURL: Optional[HttpUrl] = None
    YoutubeEmbedURL: Optional[HttpUrl] = None
    IsFeatured: bool
    ImageURLs: Optional[List[str]] = None
    Socials: Optional[List[Social]] = None
    Types: Optional[List[str]] = None
    Tags: Optional[List[str]] = None