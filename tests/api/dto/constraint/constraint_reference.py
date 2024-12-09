from typing import Optional
from pydantic import BaseModel

from api.dto.oir.nested.time.time import TimeValueDto


class ConstraintReferenceDto(BaseModel):
    id: str
    manager: str
    uss_availability: str
    version: int
    ovn: Optional[str] = None
    time_start: TimeValueDto
    time_end: TimeValueDto
    uss_base_url: str
