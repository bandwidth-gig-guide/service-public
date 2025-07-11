from fastapi import APIRouter

from uuid import UUID
from app.model.artist_brief import ArtistBrief
from app.model.artist import Artist

from app.rest.artist.get_brief import get_brief
from app.rest.artist.get_all_brief import get_all_brief
from app.rest.artist.get import get_complete
from app.rest.artist.get_all_id import get_all_id


artist = APIRouter()

# GET Single brief
@artist.get("/brief/{artist_id}", response_model=ArtistBrief)
def get_brief_(artist_id: UUID):
    return get_brief(artist_id)

# GET All briefs
@artist.get("/brief", response_model=list[ArtistBrief])
def get_all_brief_():
    return get_all_brief()

# GET Single Complete
@artist.get("/{artist_id}", response_model=Artist)
def get_complete_(artist_id: UUID):
    return get_complete(artist_id)

# GET IDs
@artist.get("/", response_model=list[UUID])
def get_all_id_():
    return get_all_id()