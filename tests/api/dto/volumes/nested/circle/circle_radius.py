from pydantic import BaseModel


class CircleRadiusDto(BaseModel):
    value: int
    units: str
