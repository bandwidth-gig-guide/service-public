from pydantic import BaseModel, HttpUrl
from typing import Optional, List
from uuid import UUID
from app.model.social import Social

class Artist(BaseModel):
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
    ImageURLs: Optional[List[HttpUrl]] = None
    Socials: Optional[List[Social]] = None
    Types: Optional[List[str]] = None
    Tags: Optional[List[str]] = None
    UpcomingEventIDs: Optional[List[UUID]] = None

def format(tuple: tuple) -> Artist:
    return Artist (
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
        Tags = tuple[13] or [],
        UpcomingEventIDs = tuple[14] or []
    )