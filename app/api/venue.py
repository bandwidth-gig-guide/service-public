from fastapi import APIRouter, Query
from typing import Optional, List
from uuid import UUID
from app.cache.redis import make_key, cache_wrap
from app.cache.key import VENUE
from app.model.venue_brief import VenueBrief
from app.model.venue import Venue

from app.rest.venue.get_brief import get_brief
from app.rest.venue.get_all_brief import get_all_brief
from app.rest.venue.get_recommended import get_recommended
from app.rest.venue.get_cities import get_cities
from app.rest.venue.get import get_complete
from app.rest.venue.get_all_id import get_all_id

venue = APIRouter()


# GET Single brief
@venue.get("/brief/{venue_id}", response_model=VenueBrief)
def get_brief_(venue_id: UUID):
    key = make_key(VENUE.BRIEF, venue_id=str(venue_id))
    return cache_wrap(key, lambda: get_brief(venue_id))


# GET All briefs
@venue.get("/brief", response_model=List[VenueBrief])
def get_all_brief_():
    key = make_key(VENUE.BRIEF)
    return cache_wrap(key, lambda: get_all_brief())


# GET Recommended
@venue.get("/recommended/{venue_id}", response_model=List[UUID])
def get_recommended_(venue_id: UUID):
    key = make_key(VENUE.RECOMMENDED, venue_id=str(venue_id))
    return cache_wrap(key, lambda: get_recommended(venue_id))


# GET All Cities
@venue.get("/cities", response_model=List[str])
def get_cities_():
    key = make_key(VENUE.CITIES)
    return cache_wrap(key, lambda: get_cities())


# GET Single Complete
@venue.get("/{venue_id}", response_model=Venue)
def get_complete_(venue_id: UUID):
    key = make_key(VENUE.DETAILED, venue_id=str(venue_id))
    return cache_wrap(key, lambda: get_complete(venue_id))


# GET IDs | Filterable
@venue.get("/", response_model=List[UUID])
def get_all_id_(
    name: Optional[str] = None,
    stateCode: Optional[str] = None,
    city: Optional[List[str]] = Query(default=None),
    types: Optional[List[str]] = Query(default=None),
    tags: Optional[List[str]] = Query(default=None),
    hasUpcomingEvent: Optional[bool] = None,
    isMonitored: Optional[bool] = None,
):
    filters = {
        "name": name,
        "stateCode": stateCode,
        "city": city,
        "types": types,
        "tags": tags,
        "hasUpcomingEvent": hasUpcomingEvent,
        "isMonitored": isMonitored,
    }
    key = make_key(VENUE.IDS, **filters)
    return cache_wrap(key, lambda: get_all_id(**filters))
