from . import is_ussp_get_oir_response_compliant
from . import CONSTRAINT_MANAGEMENT_SCOPE_VALUE
from . import UsspClient, DssClient
from . import OIR_MOCKS
from . import is_client_response_successful


class TestClassIsolatedOirInjection:

    def __get_ussp_client(self) -> UsspClient:
        return UsspClient(
            is_mocked=False, request_scope=CONSTRAINT_MANAGEMENT_SCOPE_VALUE
        )

    def __get_dss_client(self) -> DssClient:
        return DssClient(request_scope=CONSTRAINT_MANAGEMENT_SCOPE_VALUE)

    def __is_oir_object_a_match(self, dss_oir, ussp_oir) -> bool:
        ussp_oir_ref = ussp_oir["operational_intent"]["reference"]
        dss_oir_ref = dss_oir["operational_intent_reference"]

        return ussp_oir_ref is dss_oir_ref

    def test_case_isolated_oir(self) -> None:
        ussp_client = self.__get_ussp_client()
        dss_client = self.__get_dss_client()

        create_oir_ussp_response = ussp_client.put_oir(
            OIR_MOCKS.OIR_ID, OIR_MOCKS.USSP_OIR_INJECTION_REQUEST_BODY
        )

        assert is_client_response_successful(create_oir_ussp_response)

        dss_oir_response = dss_client.get_oir_by_id(OIR_MOCKS.OIR_ID)

        assert is_client_response_successful(dss_oir_response)

        ussp_oir_response = ussp_client.get_oir_by_id(OIR_MOCKS.OIR_ID)

        assert is_client_response_successful(ussp_oir_response)

        assert is_ussp_get_oir_response_compliant(ussp_oir_response)

        assert self.__is_oir_object_a_match(
            dss_oir_response.json(),
            ussp_oir_response.json(),
        )
