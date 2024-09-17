from pydantic import BaseModel
import ipaddress
from assetmodel import Source
from typing import Optional

class IPv4Netblock(BaseModel):
    cidr: ipaddress.IPv4Network
    source: Optional[Source] = None