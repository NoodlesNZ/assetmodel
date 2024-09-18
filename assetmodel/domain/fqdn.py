from pydantic import BaseModel
from assetmodel import DomainRecord, IPv4Address, IPv6Address, Source
from typing import List, Optional
from typing import ForwardRef

FQDN = ForwardRef('FQDN')

class FQDN(BaseModel):
    name: str
    source: Source
    a_record: Optional[List[IPv4Address]] = None
    aaaa_record: Optional[List[IPv6Address]] = None
    cname_record: Optional[FQDN] = None
    ns_record: Optional[List[FQDN]] = None
    mx_record: Optional[List[FQDN]] = None
    registration: Optional[DomainRecord] = None
