from pydantic import BaseModel

class AutonomousSystem(BaseModel):
    name: str
    number: int
    handle: str
