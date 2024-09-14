from pydantic import BaseModel

class NetworkEndpoint(BaseModel):
    address: str
    name: str
    port: int
    protocol: str