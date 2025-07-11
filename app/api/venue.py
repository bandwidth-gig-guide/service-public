from fastapi import APIRouter

from uuid import UUID
from app.model.venue_brief import VenueBrief
from app.model.venue import Venue

from app.rest.venue.get_brief import get_brief
from app.rest.venue.get_all_brief import get_all_brief
from app.rest.venue.get import get_complete
from app.rest.venue.get_all_id import get_all_id


venue = APIRouter()

# GET Single brief
@venue.get("/brief/{venue_id}", response_model=VenueBrief)
def get_brief_(venue_id: UUID):
    return get_brief(venue_id)

# GET All briefs
@venue.get("/brief", response_model=list[VenueBrief])
def get_all_brief_():
    return get_all_brief()

# GET Single Complete
@venue.get("/{venue_id}", response_model=Venue)
def get_complete_(venue_id: UUID):
    return get_complete(venue_id)

# GET IDs
@venue.get("/", response_model=list[UUID])
def get_all_id_():
    return get_all_id()