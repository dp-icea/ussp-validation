from . import CONSTRAINT_MANAGEMENT_SCOPE_VALUE
from . import UsspClient, DssClient
from . import OIR_MOCKS
from . import is_client_response_not_found, is_client_response_conflict


class TestClassConflictedOirInjection:

    def __get_ussp_client(self) -> UsspClient:
        return UsspClient(
            is_mocked=False, request_scope=CONSTRAINT_MANAGEMENT_SCOPE_VALUE
        )

    def __get_dss_client(self) -> DssClient:
        return DssClient(request_scope=CONSTRAINT_MANAGEMENT_SCOPE_VALUE)

    def test_setup(self, dss_client: DssClient) -> None:
        dss_client.put_oir(OIR_MOCKS.OIR_ID, OIR_MOCKS.USSP_OIR_INJECTION_REQUEST_BODY)

    def test_case_conflicted_oir(self) -> None:
        ussp_client = self.__get_ussp_client()
        dss_client = self.__get_dss_client()

        self.test_setup(dss_client)

        create_oir_ussp_response = ussp_client.put_oir(
            OIR_MOCKS.OIR_ID, OIR_MOCKS.USSP_OIR_INJECTION_REQUEST_BODY
        )

        assert is_client_response_conflict(create_oir_ussp_response)

        get_oir_dss_response = dss_client.get_oir_by_id(OIR_MOCKS.OIR_ID)

        assert is_client_response_not_found(get_oir_dss_response)
