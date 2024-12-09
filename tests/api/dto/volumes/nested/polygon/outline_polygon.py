from pydantic import BaseModel
from typing import List

from api.dto.volumes.nested.polygon.vertices import PolygonVerticesDto


class OutlinePolygonDto(BaseModel):
    vertices: List[PolygonVerticesDto]
