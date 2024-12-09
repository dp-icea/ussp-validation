from typing import Optional
from pydantic import BaseModel

from api.dto.flight_plan.nested.basic_information import BasicInformationDto
from api.dto.flight_plan.nested.operation_intent_information import (
    OperationIntentInformationDto,
)
from api.dto.flight_plan.nested.flight_authorisation_data import (
    FlightAuthorisationDataDto,
)


class FlightPlanDto(BaseModel):
    basic_information: BasicInformationDto
    astm_f3548_21: Optional[OperationIntentInformationDto] = None
    uspace_flight_authorisation: Optional[FlightAuthorisationDataDto] = None
    rpas_operating_rules_2_6: Optional[any] = (
        None  # Not defined in https://github.com/interuss/automated_testing_interfaces/tree/417797f42e8ebd7cc1b71e82ec0fee0fe1e972a1/flight_planning/v1
    )
    additional_information: Optional[dict] = None
