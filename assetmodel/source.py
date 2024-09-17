from pydantic import BaseModel

class Source(BaseModel):
    name: str
    confidence: int