from . import CONSTRAINT_MANAGEMENT_SCOPE_VALUE
from . import UsspClient
from . import is_client_response_not_found
from . import UsspOirMocks as OIR_MOCKS


class TestClassUssSuccessAuthentication:
    def __get_ussp_client(self) -> UsspClient:
        return UsspClient(
            is_mocked=False, request_scope=CONSTRAINT_MANAGEMENT_SCOPE_VALUE
        )

    def test_case_bearer_token_validation(self) -> None:
        ussp_client = self.__get_ussp_client()

        response = ussp_client.get_oir_by_id(OIR_MOCKS.INVALID_OIR_ID)

        assert is_client_response_not_found(response)
