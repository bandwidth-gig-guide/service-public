from fastapi import APIRouter, Query

from typing import Optional
from uuid import UUID
from app.model.artist_brief import ArtistBrief
from app.model.artist import Artist

from app.rest.artist.get_brief import get_brief
from app.rest.artist.get_all_brief import get_all_brief
from app.rest.artist.get import get_complete
from app.rest.artist.get_all_id import get_all_id
from app.rest.artist.get_recommended import get_recommended


artist = APIRouter()

# GET Single brief
@artist.get("/brief/{artist_id}", response_model=ArtistBrief)
def get_brief_(artist_id: UUID):
    return get_brief(artist_id)

# GET All briefs
@artist.get("/brief", response_model=list[ArtistBrief])
def get_all_brief_():
    return get_all_brief()

# GET Recommended
@artist.get("/recommended/{artist_id}", response_model=list[UUID])
def get_recommended_(artist_id: UUID):
    return get_recommended(artist_id)

# GET Single Complete
@artist.get("/{artist_id}", response_model=Artist)
def get_complete_(artist_id: UUID):
    return get_complete(artist_id)

# GET IDs | Filterable
@artist.get("/", response_model=list[UUID])
def get_all_id_(
    name: Optional[str] = None,
    country: Optional[str] = None,
    city: Optional[str] = None,
    types: Optional[list[str]] = Query(default=None),
    tags: Optional[list[str]] = Query(default=None),
    hasUpcomingEvent: Optional[bool] = None,
):
    return get_all_id(
        name=name,
        country=country,
        city=city,
        types=types,
        tags=tags,
        hasUpcomingEvent=hasUpcomingEvent
    )
