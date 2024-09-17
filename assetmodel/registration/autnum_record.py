from pydantic import BaseModel
from typing import List, Optional

class AutnumRecord(BaseModel):
    raw: Optional[str] = None
    number: int
    handle: Optional[str] = None
    name: Optional[str] = None
    whois_server: Optional[str] = None
    created_date: Optional[str] = None
    updated_date: Optional[str] = None
    status: Optional[List[str]] = None