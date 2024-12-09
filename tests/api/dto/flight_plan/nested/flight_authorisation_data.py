from typing import List, Optional
from pydantic import BaseModel


class FlightAuthorisationDataDto(BaseModel):
    uas_serial_number: str
    operation_mode: str
    operation_category: str
    uas_class: str
    identification_technologies: List[str]
    uas_type_certificate: Optional[str] = None
    connectivity_methods: List[str]
    endurance_minutes: int
    emergency_procedure_url: str
    operator_id: str
    uas_id: Optional[str] = None
