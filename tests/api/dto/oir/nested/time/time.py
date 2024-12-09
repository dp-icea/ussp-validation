from pydantic import BaseModel


class TimeValueDto(BaseModel):
    value: str
    format: str
