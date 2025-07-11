from pydantic import BaseModel, HttpUrl

class Social(BaseModel):
    SocialPlatform: str
    Handle: str
    URL: HttpUrl