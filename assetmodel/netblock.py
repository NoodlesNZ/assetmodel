from pydantic import BaseModel
from assetmodel.type import NetblockType

class Netblock(BaseModel):
    cidr: str
    type: NetblockType