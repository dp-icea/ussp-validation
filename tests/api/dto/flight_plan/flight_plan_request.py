from pydantic import BaseModel

from api.dto.flight_plan.nested.flight_plan import FlightPlanDto


class FlightPlanInjectionDto(BaseModel):
    flight_plan: FlightPlanDto
    execution_style: str
    request_id: str
