from pydantic import BaseModel
from typing import List, Optional

class DomainRecord(BaseModel):
    raw: Optional[str]
    id: Optional[str]
    domain: Optional[str]
    punycode: Optional[str]
    name: Optional[str]
    extension: Optional[str]
    whois_server: Optional[str]
    created_date: Optional[str]
    updated_date: Optional[str]
    expiration_date: Optional[str]
    status: Optional[List[str]]
    dnssec: Optional[bool]