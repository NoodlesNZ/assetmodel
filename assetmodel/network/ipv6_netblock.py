from pydantic import BaseModel
import ipaddress
from assetmodel import Source
from typing import Optional

class IPv6Netblock(BaseModel):
    cidr: ipaddress.IPv6Network
    source: Optional[Source] = None