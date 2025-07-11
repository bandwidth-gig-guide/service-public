from fastapi import FastAPI
from fastapi.exceptions import HTTPException


from app.api.artist import artist
from app.api.artist_card import artist_card
from app.api.artist_complete import artist_complete

from app.api.venue import venue
from app.api.venue_card import venue_card
from app.api.venue_complete import venue_complete


from app.core.handle.exception import handle_exception
from app.core.handle.http_exception import handle_http_exception


app = FastAPI()

# Artist Routes
app.include_router(artist, prefix="/artist", tags=["artist"])
app.include_router(artist_card, prefix="/artist/card", tags=["artist_card"])
app.include_router(artist_complete, prefix="/artist/complete", tags=["artist_complete"])

# Venue Routes
app.include_router(venue, prefix="/venue", tags=["venue"])
app.include_router(venue_card, prefix="/venue/card", tags=["venue_card"])
app.include_router(venue_complete, prefix="/venue/complete", tags=["venue_complete"])


# Handlers
app.add_exception_handler(Exception, handle_exception)
app.add_exception_handler(HTTPException, handle_http_exception)