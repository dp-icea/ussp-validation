from typing import List
from pydantic import BaseModel

from api.dto.constraint.constraint_reference import ConstraintReferenceDto


class PutConstraintResponseDto(BaseModel):
    subscribers: List[any]  # TODO: create subscribers dto
    constraint_reference: ConstraintReferenceDto
