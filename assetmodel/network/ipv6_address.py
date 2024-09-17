from pydantic import BaseModel
import ipaddress
from assetmodel import IPv6Netblock, Source
from typing import Optional

class IPv6Address(BaseModel):
    address: ipaddress.IPv6Address
    netblock: Optional[IPv6Netblock] = None
    source: Source
