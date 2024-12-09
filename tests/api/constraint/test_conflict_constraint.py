from . import CONSTRAINT_MANAGEMENT_SCOPE_VALUE
from . import DssConstraintMocks as CONSTRAINT_MOCKS
from . import UsspClient, DssClient
from . import is_client_response_conflict, is_client_response_not_found
from . import UsspFlighPlanMocks as FLIGHT_PLAN_MOCKS


class TestClassOirConflictConstraint:
    def __get_ussp_client(self) -> UsspClient:
        return UsspClient(
            is_mocked=False, request_scope=CONSTRAINT_MANAGEMENT_SCOPE_VALUE
        )

    def __get_dss_client(self) -> DssClient:
        return DssClient(request_scope=CONSTRAINT_MANAGEMENT_SCOPE_VALUE)

    def test_setup(self, dss_client: DssClient) -> None:
        dss_client.put_constraint(CONSTRAINT_MOCKS.DSS_PUT_CONSTRAINT_REQUEST_BODY)

    def test_case_oir_conflict_with_constraint(self) -> None:
        ussp_client = self.__get_ussp_client()
        dss_client = self.__get_dss_client()

        self.test_setup(dss_client)

        oir_injection_response = ussp_client.put_oir(
            FLIGHT_PLAN_MOCKS.FLIGHT_PLAN_ID,
            FLIGHT_PLAN_MOCKS.USSP_PUT_FLIGHT_PLAN_REQUEST_BODY,
        )

        assert is_client_response_conflict(oir_injection_response)

        get_oir_dss_response = dss_client.get_oir_by_id(
            FLIGHT_PLAN_MOCKS.FLIGHT_PLAN_ID
        )

        assert is_client_response_not_found(get_oir_dss_response)
