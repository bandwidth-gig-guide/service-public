from pydantic import BaseModel, HttpUrl
from typing import Optional
from uuid import UUID

class VenueBrief(BaseModel):
    VenueID: UUID
    Title: str
    City: str
    StreetAddress: str
    StateCode: str
    PostCode: int
    IsFeatured: bool
    ImageUrl: Optional[HttpUrl] = None
    UpcomingEventCount: int

def format(tuple: tuple) -> VenueBrief:
    return VenueBrief (
        VenueID = tuple[0],
        Title = tuple[1],
        City = tuple[2],
        StreetAddress = tuple[3],
        StateCode = tuple[4],
        PostCode = tuple[5],
        IsFeatured = tuple[6],
        ImageUrl = tuple[7],
        UpcomingEventCount = tuple[8]
    )