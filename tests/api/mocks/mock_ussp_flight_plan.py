from . import FlightPlanInjectionDto
from . import usage_state_switcher, uas_state_switcher
from . import VolumeMocks
from . import FlightPlanMocks

from uuid import uuid4


class UsspFlighPlanMocks:
    FLIGHT_PLAN_ID: str = "f4959f12-1fa0-41cc-931f-d66866847563"

    USSP_PUT_FLIGHT_PLAN_PLANNED_STATE_REQUEST_BODY: FlightPlanInjectionDto = {
        "flight_plan": {
            "basic_information": {
                "usage_state": usage_state_switcher["PLANNED"],
                "uas_state": uas_state_switcher["NOMINAL"],
                "area": [VolumeMocks.VOLUME_4D],
            },
            "astm_f3548_21": FlightPlanMocks.ASTM_F3548_21_OP_INTENT,
            "uspace_flight_authorisation": FlightPlanMocks.USPACE_FLIGHT_AUTH_DATA,
        },
        "execution_style": "IfAllowed",
        "request_id": uuid4(),
    }

    USSP_PUT_FLIGHT_PLAN_IN_USE_STATE_REQUEST_BODY: FlightPlanInjectionDto = {
        "flight_plan": {
            "basic_information": {
                "usage_state": usage_state_switcher["IN_USE"],
                "uas_state": uas_state_switcher["NOMINAL"],
                "area": [VolumeMocks.VOLUME_4D],
            },
            "astm_f3548_21": FlightPlanMocks.ASTM_F3548_21_OP_INTENT,
            "uspace_flight_authorisation": FlightPlanMocks.USPACE_FLIGHT_AUTH_DATA,
        },
        "execution_style": "IfAllowed",
        "request_id": uuid4(),
    }
