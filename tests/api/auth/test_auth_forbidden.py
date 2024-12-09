from . import INVALID_SCOPE_VALUE
from . import UsspClient
from . import is_client_response_forbidden
from . import UsspOirMocks as OIR_MOCKS


class TestClassUssForbiddenAuthentication:
    def __get_ussp_client(self) -> UsspClient:
        return UsspClient(is_mocked=True, request_scope=INVALID_SCOPE_VALUE)

    def test_case_bearer_token_validation(self) -> None:
        ussp_client = self.__get_ussp_client()

        response = ussp_client.get_oir_by_id(OIR_MOCKS.OIR_ID)

        assert is_client_response_forbidden(response)
