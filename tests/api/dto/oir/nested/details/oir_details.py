from api.dto.volumes.volume_4d import Volume4dDto

from pydantic import BaseModel
from typing import Optional


class OirDetailsDto(BaseModel):
    volumes: Optional[Volume4dDto] = None
    off_nominal_volumes: Optional[Volume4dDto] = None
    priority: Optional[int] = None
