from fastapi import FastAPI
from fastapi.exceptions import HTTPException

from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from starlette.middleware.proxy_headers import ProxyHeadersMiddleware

from app.api.artist import artist
from app.api.event import event
from app.api.venue import venue

from app.core.handle.exception import handle_exception
from app.core.handle.http_exception import handle_http_exception

# App
app = FastAPI()
app.add_middleware(ProxyHeadersMiddleware, trusted_hosts="*")


# Routes
app.include_router(artist, prefix="/public/artist", tags=["artist"])
app.include_router(event, prefix="/public/event", tags=["event"])
app.include_router(venue, prefix="/public/venue", tags=["venue"])

# Handlers
app.add_exception_handler(Exception, handle_exception)
app.add_exception_handler(HTTPException, handle_http_exception)