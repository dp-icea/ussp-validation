from pydantic import BaseModel

from api.dto.volumes.volume_4d import Volume4dDto


class BasicInformationDto(BaseModel):
    usage_state: str
    uas_state: str
    area: Volume4dDto
