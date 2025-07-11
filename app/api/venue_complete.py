from fastapi import APIRouter
from uuid import UUID
from app.model.venue_complete import VenueComplete
from app.rest.venue_complete.get import get

venue_complete = APIRouter()

# GET
@venue_complete.get("/{venue_id}", response_model=VenueComplete)
def get_(venue_id: UUID):
    return get(venue_id)