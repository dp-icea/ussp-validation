from pydantic import BaseModel


class OperationIntentInformationDto(BaseModel):
    priority: int
