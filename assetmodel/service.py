from pydantic import BaseModel

class Service(BaseModel):
    identifier: str
    version: str