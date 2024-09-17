from pydantic import BaseModel
import ipaddress
from assetmodel import IPv4Network, Source
from typing import Optional

class IPv4Address(BaseModel):
    address: ipaddress.IPv4Address
    netblock: Optional[IPv4Network] = None
    source: Source
