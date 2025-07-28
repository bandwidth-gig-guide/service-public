from fastapi import APIRouter, Query

from typing import Optional
from uuid import UUID
from datetime import date
from app.model.event_brief import EventBrief
from app.model.event import Event

from app.rest.event.get_brief import get_brief
from app.rest.event.get_all_brief import get_all_brief
from app.rest.event.get import get_complete
from app.rest.event.get_all_id import get_all_id


event = APIRouter()

# GET Single brief
@event.get("/brief/{event_id}", response_model=EventBrief)
def get_brief_(event_id: UUID):
    return get_brief(event_id)

# GET All briefs
@event.get("/brief", response_model=list[EventBrief])
def get_all_brief_():
    return get_all_brief()

# GET Single Complete
@event.get("/{event_id}", response_model=Event)
def get_complete_(event_id: UUID):
    return get_complete(event_id)

# GET IDs
@event.get("/", response_model=list[UUID])
def get_all_id_(
    name: Optional[str] = None,
    stateCode: Optional[str] = None,
    city: Optional[list[str]] = Query(default=None),
    maxPrice: Optional[int] = None,
    types: Optional[list[str]] = Query(default=None),
    tags: Optional[list[str]] = Query(default=None),
    dates: Optional[list[date]] = Query(default=None)
):
    return get_all_id(
        name=name,
        stateCode=stateCode,
        city=city,
        maxPrice=maxPrice,
        types=types,
        tags=tags,
        dates=dates
    )