from pydantic import BaseModel

class FQDN(BaseModel):
    name: str