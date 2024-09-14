from pydantic import BaseModel

class SocketAddress(BaseModel):
    address: str
    ip_address: str
    port: int
    protocol: str