from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class VenueCard(BaseModel):
    VenueID: UUID
    Title: str
    City: str
    StreetAddress: str
    StateCode: str
    PostCode: int
    IsFeatured: bool
    ImageURL: Optional[str] = None
    UpcomingEventCount: int