from pydantic import BaseModel, HttpUrl
from typing import Optional
from uuid import UUID

class ArtistBrief(BaseModel):
    ArtistID: UUID
    Title: str
    Country: str
    City: str
    IsFeatured: bool
    IsResearched: bool
    ImageUrl: Optional[HttpUrl] = None
    UpcomingEvents: int

def format(tuple: tuple) -> ArtistBrief:
    return ArtistBrief (
        ArtistID = tuple[0],
        Title = tuple[1],
        Country = tuple[2],
        City = tuple[3],
        IsFeatured = tuple[4],
        IsResearched = tuple[5],
        ImageUrl = tuple[6],
        UpcomingEvents = tuple[7]
    )