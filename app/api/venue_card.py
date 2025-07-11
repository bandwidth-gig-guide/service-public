from fastapi import APIRouter
from uuid import UUID
from app.model.venue_card import VenueCard
from app.rest.venue_card.get import get
from app.rest.venue_card.get_all import get_all

venue_card = APIRouter()

# GET ALL
@venue_card.get("/", response_model=list[VenueCard])
def get_all_():
    return get_all()

# GET
@venue_card.get("/{venue_id}", response_model=VenueCard)
def get_(venue_id: UUID):
    return get(venue_id)