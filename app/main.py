from fastapi import FastAPI
from fastapi.exceptions import HTTPException

from app.api.venue import venue
from app.api.venue_card import venue_card

from app.core.handle.exception import handle_exception
from app.core.handle.http_exception import handle_http_exception


app = FastAPI()

# Routes
app.include_router(venue, prefix="/venue", tags=["venue"])
app.include_router(venue_card, prefix="/venue/card", tags=["venue_card"])

# Handlers
app.add_exception_handler(Exception, handle_exception)
app.add_exception_handler(HTTPException, handle_http_exception)