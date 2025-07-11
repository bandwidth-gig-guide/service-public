from fastapi import Request
from fastapi.responses import JSONResponse

async def handle_exception(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"detail": "Internal Server Error"})