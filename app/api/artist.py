from fastapi import APIRouter
from uuid import UUID
from app.rest.artist.get_ids import get_ids

artist = APIRouter()

# GET IDs
@artist.get("/", response_model=list[UUID])
def get_ids_():
    return get_ids()
