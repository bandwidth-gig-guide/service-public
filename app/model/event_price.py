from pydantic import BaseModel

class EventPrice(BaseModel):
    TicketType: str
    Price: float
