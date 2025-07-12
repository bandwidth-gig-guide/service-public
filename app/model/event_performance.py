from pydantic import BaseModel, HttpUrl
from uuid import UUID
from datetime import datetime

class EventPerformance(BaseModel):
    ArtistID: UUID
    Title: str
    ImageUrl: HttpUrl
    SetListPosition: int
    StartDateTime: datetime