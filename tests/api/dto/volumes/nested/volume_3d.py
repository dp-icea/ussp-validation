from api.dto.volumes.nested.altitude import AltitudeDto
from api.dto.volumes.nested.circle.outline_circle import OutlineCircleDto
from api.dto.volumes.nested.polygon.outline_polygon import OutlinePolygonDto

from pydantic import BaseModel
from typing import Optional


class Volume3dDto(BaseModel):
    outline_circle: Optional[OutlineCircleDto] = None
    outline_polygon: Optional[OutlinePolygonDto] = None
    altitude_lower: AltitudeDto
    altitude_upper: AltitudeDto
