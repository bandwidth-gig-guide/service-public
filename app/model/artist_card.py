from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class ArtistCard(BaseModel):
    ArtistID: UUID
    Title: str
    Country: str
    City: str
    IsFeatured: bool
    ImageURL: Optional[str] = None
    UpcomingEvents: int