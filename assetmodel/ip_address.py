from pydantic import BaseModel
from assetmodel.type import IpAddressType

class IpAddress(BaseModel):
    address: str
    type: IpAddressType
