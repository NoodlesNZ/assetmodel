from pydantic import BaseModel
import ipaddress
from assetmodel import IPv4Netblock, Source
from typing import Optional

class IPv4Address(BaseModel):
    address: ipaddress.IPv4Address
    netblock: Optional[IPv4Netblock] = None
    source: Optional[Source] = None
