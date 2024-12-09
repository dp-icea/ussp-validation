from pydantic import BaseModel


class CircleCenterDto(BaseModel):
    value: int
    units: str
