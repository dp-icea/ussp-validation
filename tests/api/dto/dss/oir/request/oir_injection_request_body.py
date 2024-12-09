from typing import Optional
from api.dto.volumes.volume_4d import Volume4dDto
from dataclasses import dataclass


@dataclass
class OirInjectionRequestDto:
    flight_type: str
    extents: Volume4dDto
    key: Optional[str] = None
    state: str
    uss_base_url: str
    subscription_id: str
