from api.dto.oir.nested.reference.reference import OirReferenceDto
from pydantic import BaseModel


class OperationalIntentDto(BaseModel):
    reference: OirReferenceDto
