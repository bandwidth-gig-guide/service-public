from fastapi import FastAPI
from fastapi.exceptions import HTTPException

from app.api.artist import artist
from app.api.event import event
from app.api.venue import venue

from app.core.handle.exception import handle_exception
from app.core.handle.http_exception import handle_http_exception

# App
app = FastAPI()

# Routes
app.include_router(artist, prefix="/artist", tags=["artist"])
app.include_router(event, prefix="/event", tags=["event"])
app.include_router(venue, prefix="/venue", tags=["venue"])

# Handlers
app.add_exception_handler(Exception, handle_exception)
app.add_exception_handler(HTTPException, handle_http_exception)