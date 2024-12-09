from pydantic import BaseModel
from api.dto.volumes.nested.circle.circle_center import CircleCenterDto
from api.dto.volumes.nested.circle.circle_radius import CircleRadiusDto


class OutlineCircleDto(BaseModel):
    center: CircleCenterDto
    radius: CircleRadiusDto
