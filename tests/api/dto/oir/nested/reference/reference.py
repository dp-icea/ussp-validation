from pydantic import BaseModel
from api.dto.oir.nested.time.time import TimeValueDto


class OirReferenceDto(BaseModel):
    id: str
    flight_type: str
    manager: str
    uss_availability: str
    version: int
    state: str
    ovn: str
    time_start: TimeValueDto
    time_end: TimeValueDto
    uss_base_url: str
    subscription_id: str
