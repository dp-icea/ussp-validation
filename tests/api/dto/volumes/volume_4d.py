from api.dto.oir.nested.time.time import TimeValueDto
from api.dto.volumes.nested.volume_3d import Volume3dDto
from pydantic import BaseModel


class Volume4dDto(BaseModel):
    volume: Volume3dDto
    time_start: TimeValueDto
    time_end: TimeValueDto
