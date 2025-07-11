from pydantic import BaseModel, HttpUrl
from typing import Optional, List
from uuid import UUID
from datetime import datetime

class EventBrief(BaseModel):
    EventID: UUID
    Title: str
    StartDateTime: datetime
    VenueTitle: str
    IsFeatured: bool
    ImageURL: Optional[HttpUrl] = None
    ArtistTitles: List[str]
    MinPrice: int

def format(tuple: tuple) -> EventBrief:
    return EventBrief (
        EventID = tuple[0],
        Title = tuple[1],
        StartDateTime = tuple[2],
        VenueTitle = tuple[3],
        IsFeatured = tuple[4],
        ImageURL = tuple[5],
        ArtistTitles = tuple[6],
        MinPrice = tuple[7]
    )