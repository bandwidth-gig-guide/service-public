from fastapi import APIRouter
from uuid import UUID
from app.model.artist_complete import ArtistComplete
from app.rest.artist_complete.get import get

artist_complete = APIRouter()

# GET
@artist_complete.get("/{artist_id}", response_model=ArtistComplete)
def get_(artist_id: UUID):
    return get(artist_id)