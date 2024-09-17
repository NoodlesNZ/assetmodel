from pydantic import BaseModel
from typing import List, Optional
from datetime import date

class AutnumRecord(BaseModel):
    raw: Optional[str] = None
    number: int
    handle: Optional[str] = None
    name: Optional[str] = None
    whois_server: Optional[str] = None
    created_date: Optional[date] = None
    updated_date: Optional[date] = None
    status: Optional[List[str]] = None