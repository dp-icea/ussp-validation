from os import environ
from . import (
    QUERY_PARAM_API_KEY_NAME,
    QUERY_PARAM_INTENDED_AUDIENCE_NAME,
    QUERY_PARAM_SCOPE_NAME,
)
from . import AuthenticationMocks
from api.utils.config.token_parameters_switch import audience_switcher


class AuthenticationHeaderBuilder:
    def __init__(self, is_mocked: bool, scope: str, client_type: bool):
        self.bearer_token_req_params = self.__build_request_bearer_token_parameters(
            is_mocked, scope, client_type
        )

    def __build_request_bearer_token_parameters(
        self, is_mocked: bool, scope: str, client_type: str
    ) -> str:
        return (
            self.__build_mocked_token_request_query_parameters()
            if is_mocked
            else self.__build_valid_token_request_query_parameters(scope, client_type)
        )

    def __build_mocked_token_request_query_parameters(self) -> dict:
        return AuthenticationMocks.INVALID_TOKEN_REQUEST_PARAMETER_STR

    def __build_token_audience(self, client_type: str) -> str:
        return audience_switcher.get(client_type)

    def __build_valid_token_request_query_parameters(
        self, scope: str, client_type: str
    ) -> dict:
        return {
            QUERY_PARAM_SCOPE_NAME: scope,
            QUERY_PARAM_INTENDED_AUDIENCE_NAME: self.__build_token_audience(
                client_type
            ),
            QUERY_PARAM_API_KEY_NAME: environ.get("DSS_API_KEY"),
        }

    def get_request_bearer_token_parameters(self) -> str:
        return self.bearer_token_req_params
