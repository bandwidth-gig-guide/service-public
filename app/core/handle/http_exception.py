from fastapi import Request
from fastapi.exceptions import HTTPException
from fastapi.exception_handlers import http_exception_handler

async def handle_http_exception(request: Request, exc: HTTPException):
    return await http_exception_handler(request, exc)