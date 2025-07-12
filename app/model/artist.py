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
    SpotifyEmbedUrl: Optional[HttpUrl] = None
    YoutubeEmbedUrl: Optional[HttpUrl] = None
    IsFeatured: bool
    ImageUrls: Optional[List[HttpUrl]] = None
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
        SpotifyEmbedUrl = tuple[7],
        YoutubeEmbedUrl = tuple[8],
        IsFeatured = tuple[9],
        ImageUrls = tuple[10] or [],
        Socials = tuple[11] or [],
        Types = tuple[12] or [],
        Tags = tuple[13] or [],
        UpcomingEventIDs = tuple[14] or []
    )