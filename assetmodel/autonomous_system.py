from pydantic import BaseModel
from assetmodel import AutnumRecord, IPv4Netblock, IPv6Netblock
from typing import List, Optional

class AutonomousSystem(BaseModel):
    number: int
    registration: AutnumRecord
    announces_ipv4: Optional[List[IPv4Netblock]] = None
    announces_ipv6: Optional[List[IPv6Netblock]] = None
