from pydantic import BaseModel

class Fingerprint(BaseModel):
    value: str
    type: str