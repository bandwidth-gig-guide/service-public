from pydantic import BaseModel
from datetime import time

class OpeningHours(BaseModel):
    MonOpen: time
    MonClose: time
    TueOpen: time
    TueClose: time
    WedOpen: time
    WedClose: time
    ThurOpen: time
    ThurClose: time
    FriOpen: time
    FriClose: time
    SatOpen: time
    SatClose: time
    SunOpen: time
    SunClose: time