from fastapi import APIRouter
from uuid import UUID
from app.model.artist_card import ArtistCard
from app.rest.artist_card.get import get
from app.rest.artist_card.get_all import get_all

artist_card = APIRouter()

# GET ALL
@artist_card.get("/", response_model=list[ArtistCard])
def get_all_():
    return get_all()

# GET
@artist_card.get("/{artist_id}", response_model=ArtistCard)
def get_(artist_id: UUID):
    return get(artist_id)