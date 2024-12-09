from api.dto.ussp.oir.response.operational_intent import OperationalIntentDto
from pydantic import BaseModel


class GetOirByIdDto(BaseModel):
    operational_intent: OperationalIntentDto
