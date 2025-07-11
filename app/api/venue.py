from fastapi import APIRouter
from uuid import UUID
from app.rest.venue.get_ids import get_ids

venue = APIRouter()

# GET IDs
@venue.get("/", response_model=list[UUID])
def get_ids_():
    return get_ids()
