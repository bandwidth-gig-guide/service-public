from pydantic import BaseModel, HttpUrl
from typing import Optional, List
from uuid import UUID
from datetime import datetime
from app.model.event_price import EventPrice
from app.model.event_venue import EventVenue
from app.model.event_performance import EventPerformance
from app.model.social import Social

class Event(BaseModel):
    EventID: UUID
    Title: str
    StartDateTime: datetime
    Description: str
    OriginalPostUrl: HttpUrl
    TicketSaleUrl: HttpUrl
    IsFeatured: bool
    ImageUrls: Optional[List[HttpUrl]] = None
    Socials: Optional[List[Social]] = None
    Types: Optional[List[str]] = None
    Tags: Optional[List[str]] = None
    Venue: EventVenue
    Performances: List[EventPerformance]
    Prices: List[EventPrice]

def format(tuple: tuple) -> Event:
    return Event (
        EventID = tuple[0],
        Title = tuple[1],
        StartDateTime = tuple[2],
        Description = tuple[3],
        OriginalPostUrl = tuple[4],
        TicketSaleUrl = tuple[5],
        IsFeatured = tuple[6],
        ImageUrls = tuple[7] or [],
        Socials = tuple[8] or [],
        Types = tuple[9] or [],
        Tags = tuple[10] or [],
        Venue = tuple[11],
        Performances = tuple[12] or [],
        Prices = tuple[13] or []
    )
