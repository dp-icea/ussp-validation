from pydantic import BaseModel


class PolygonVerticesDto(BaseModel):
    lng: int
    lat: int
