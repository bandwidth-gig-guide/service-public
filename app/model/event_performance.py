from pydantic import BaseModel, HttpUrl
from uuid import UUID
from datetime import datetime
from typing import Optional

class EventPerformance(BaseModel):
    ArtistID: UUID
    Title: str
    ImageUrl: Optional[HttpUrl] = None
    SetListPosition: int
    StartDateTime: datetime