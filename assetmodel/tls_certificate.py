from typing import List, Optional
from pydantic import BaseModel

class TlsCertificate(BaseModel):
    raw: Optional[str] = None
    version: str
    serial_number: str
    subject_common_name: str
    issuer_common_name: str
    not_before: str
    not_after: str
    key_usage: List[str]
    signature_algorithm: str
    public_key_algorithm: str
    is_ca: bool
    crl_distribution_points: List[str]
    subject_key_id: str
    authority_key_id: str
