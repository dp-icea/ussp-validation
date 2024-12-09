from pydantic import BaseModel


class AltitudeDto(BaseModel):
    value: int
    reference: str
    units: str
