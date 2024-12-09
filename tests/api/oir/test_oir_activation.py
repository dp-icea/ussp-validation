from . import is_client_response_successful, usage_state_switcher
from . import CONSTRAINT_MANAGEMENT_SCOPE_VALUE
from . import UsspClient, DssClient
from . import FLIGHT_PLAN_MOCKS
from . import GetDssOirByIdDto


class TestClassOirActivation:

    def __get_ussp_client(self) -> UsspClient:
        return UsspClient(
            is_mocked=False, request_scope=CONSTRAINT_MANAGEMENT_SCOPE_VALUE
        )

    def __get_dss_client(self) -> DssClient:
        return DssClient(request_scope=CONSTRAINT_MANAGEMENT_SCOPE_VALUE)

    def __is_flight_plan_in_use(self, oir: GetDssOirByIdDto) -> bool:
        return (
            oir["flight_plan"]["basic_information"]["usage_state"]
            == usage_state_switcher["IN_USE"],
        )

    def test_setup(self, ussp_client: UsspClient) -> None:
        ussp_client.put_oir(
            FLIGHT_PLAN_MOCKS.FLIGHT_PLAN_ID,
            FLIGHT_PLAN_MOCKS.USSP_PUT_FLIGHT_PLAN_PLANNED_STATE_REQUEST_BODY,
        )

    def test_case_oir_activation(self) -> None:
        ussp_client = self.__get_ussp_client()
        dss_client = self.__get_dss_client()

        self.test_setup(ussp_client)

        get_oir_dss_response = dss_client.get_oir_by_id(
            FLIGHT_PLAN_MOCKS.FLIGHT_PLAN_ID
        )

        assert is_client_response_successful(get_oir_dss_response)

        ussp_client.put_oir(
            FLIGHT_PLAN_MOCKS.FLIGHT_PLAN_ID,
            FLIGHT_PLAN_MOCKS.USSP_PUT_FLIGHT_PLAN_IN_USE_STATE_REQUEST_BODY,
        )

        get_oir_dss_response = dss_client.get_oir_by_id(
            FLIGHT_PLAN_MOCKS.FLIGHT_PLAN_ID
        )

        assert is_client_response_successful(
            get_oir_dss_response
        ) and self.__is_flight_plan_in_use(get_oir_dss_response.json())
