from os import environ
from requests import Request, Response
from api.utils.client.client_session_config import ClientSessionConfig
from . import AuthenticationHeaderBuilder
from . import GET_TOKEN_PATH
import logging


class AuthenticationClient:
    logger = logging.getLogger("http_logger")

    def __init__(self, is_mocked: bool, scope: str, client_type: str):
        self.base_url: str = environ.get("KONG_URL")
        self.session = ClientSessionConfig().get_client_session()
        self.auth_header_builder = AuthenticationHeaderBuilder(
            is_mocked, scope, client_type
        )

    def get_bearer_token(self) -> Response:
        url = self.base_url + GET_TOKEN_PATH
        params = self.auth_header_builder.get_request_bearer_token_parameters()

        req = Request("GET", url, data={}, params=params, headers=self.session.headers)
        prepped_req = self.session.prepare_request(req)
        self.logger.info(prepped_req.headers)

        try:
            response = self.session.send(prepped_req)
            self.logger.info(response.json())

            return response
        except Exception as err:
            self.logger.error(err)
            raise err
