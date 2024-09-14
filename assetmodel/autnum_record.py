from pydantic import BaseModel
from typing import List, Optional

class AutnumRecord(BaseModel):
    raw: Optional[str]
    number: int
    handle: Optional[str]
    name: Optional[str]
    whois_server: Optional[str]
    created_date: Optional[str]
    updated_date: Optional[str]
    status: Optional[List[str]]