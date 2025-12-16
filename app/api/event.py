from fastapi import APIRouter, Query

from typing import Optional, List, Dict
from uuid import UUID
from datetime import date
from app.cache.redis import make_key, cache_wrap
from app.cache.key import EVENT
from app.model.event_brief import EventBrief
from app.model.event import Event

from app.rest.event.get_brief import get_brief
from app.rest.event.get_all_brief import get_all_brief
from app.rest.event.get_recommended import get_recommended
from app.rest.event.get import get_complete
from app.rest.event.get_all_id import get_all_id
from app.rest.event.get_all_id_by_date import get_all_id_by_date


event = APIRouter()


# GET Single brief
@event.get("/brief/{event_id}", response_model=EventBrief)
def get_brief_(event_id: UUID):
    key = make_key(EVENT.BRIEF, artist_id=str(event_id))
    return cache_wrap(key, lambda: get_brief(event_id))


# GET All briefs
@event.get("/brief", response_model=list[EventBrief])
def get_all_brief_():
    key = make_key(EVENT.BRIEF)
    return cache_wrap(key, lambda: get_all_brief())


# GET Recommended
@event.get("/recommended/{event_id}", response_model=list[UUID])
def get_recommended_(event_id: UUID):
    key = make_key(EVENT.RECOMMENDED, event_id=str(event_id))
    return cache_wrap(key, lambda: get_recommended(event_id))


# GET IDs Grouped By Date
@event.get("/by-date", response_model=Dict[date, List[UUID]])
def get_all_id__by_date_(
    name: Optional[str] = None,
    stateCode: Optional[str] = None,
    city: Optional[list[str]] = Query(default=None),
    maxPrice: Optional[int] = None,
    types: Optional[list[str]] = Query(default=None),
    tags: Optional[list[str]] = Query(default=None),
    dates: Optional[list[date]] = Query(default=None)
):
    filters = {
        "name": name,
        "stateCode": stateCode,
        "city": city,
        "maxPrice": maxPrice,
        "types": types,
        "tags": tags,
        "dates": dates
    }
    key = make_key(EVENT.IDS_BY_DATE, **filters)
    return cache_wrap(key, lambda: get_all_id_by_date(**filters))


# GET Single Complete
@event.get("/{event_id}", response_model=Event)
def get_complete_(event_id: UUID):
    key = make_key(EVENT.DETAILED, event_id=str(event_id))
    return cache_wrap(key, lambda: get_complete(event_id))


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
    filters = {
        "name": name,
        "stateCode": stateCode,
        "city": city,
        "maxPrice": maxPrice,
        "types": types,
        "tags": tags,
        "dates": dates
    }
    key = make_key(EVENT.IDS, **filters)
    return cache_wrap(key, lambda: get_all_id(**filters))
