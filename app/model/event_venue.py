from pydantic import BaseModel, HttpUrl
from uuid import UUID

class EventVenue(BaseModel):
    VenueID: UUID
    Title: str
    StageTitle: str
    ImageURL: HttpUrl
