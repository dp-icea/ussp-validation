from typing import List
from pydantic import BaseModel

from api.dto.volumes.volume_4d import Volume4dDto


class PutConstraintRequestDto(BaseModel):
    extents: List[Volume4dDto]
    uss_base_url: str
