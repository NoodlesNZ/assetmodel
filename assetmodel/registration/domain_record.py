from pydantic import BaseModel
from typing import List, Optional
from datetime import date

class DomainRecord(BaseModel):
    raw: Optional[str] = None
    id: Optional[str] = None
    domain: Optional[str] = None
    punycode: Optional[str] = None
    name: Optional[str] = None
    extension: Optional[str] = None
    whois_server: Optional[str] = None
    created_date: Optional[date] = None
    updated_date: Optional[date] = None
    expiration_date: Optional[date] = None
    status: Optional[List[str]] = None
    dnssec: Optional[bool] = None