from os import environ
import logging
from requests import Request, Response
from uuid import uuid4

from api.utils.client.client_session_config import ClientSessionConfig
from api.utils.client.auth_client import AuthenticationClient

from . import OirInjectionRequestDto, PutConstraintRequestDto
from . import DSS_CLIENT_TYPE


class DssClient:
    logger = logging.getLogger("http_logger")

    def __init__(self, request_scope: str):
        self.base_url = environ.get("DSS_URL")
        self.session = ClientSessionConfig().get_client_session()
        self.auth_client = AuthenticationClient(
            is_mocked=False, scope=request_scope, client_type=DSS_CLIENT_TYPE
        )

    def __get_bearer_token(self) -> Response:
        return self.auth_client.get_bearer_token()

    def __set_authentication_headers(self) -> None:
        bearer_token = self.__get_bearer_token().json()["access_token"]
        self.session.headers.update({"Authorization": "Bearer" + str(bearer_token)})

    def get_oir_by_id(self, oir_id: str) -> Response:
        self.__set_authentication_headers()
        url = self.base_url + f"/dss/v1/operational_intent_references/${oir_id}"

        req = Request("GET", url, data={})
        prepped_req = self.session.prepare_request(req)
        self.logger.info(prepped_req.headers)

        try:
            response = self.session.send(prepped_req)
            self.logger.info(response.json())

            return response
        except Exception as err:
            self.logger.error(err)
            raise err

    def put_oir(self, oir_id: str, request_body: OirInjectionRequestDto) -> Response:
        self.__set_authentication_headers()
        url = self.base_url + f"/dss/v1/operational_intent_references/{oir_id}"

        req = Request("PUT", url, data=request_body)
        prepped_req = self.session.prepare_request(req)
        self.logger.info(prepped_req.headers)
        self.logger.info(prepped_req.body)

        try:
            response = self.session.send(prepped_req)
            self.logger.info(response.json())

            return response
        except Exception as err:
            self.logger.error(err)
            raise err

    def put_constraint(self, request_body: PutConstraintRequestDto) -> Response:
        self.__set_authentication_headers()

        entity_id = uuid4()
        url = self.base_url + f"/dss/v1/constraint_references/{entity_id}"

        req = Request("PUT", url, data=request_body)
        prepped_req = self.session.prepare_request(req)
        self.logger.info(prepped_req.headers)
        self.logger.info(prepped_req.body)

        try:
            response = self.session.send(prepped_req)
            self.logger.info(response.json())

            return response
        except Exception as err:
            self.logger.error(err)
            raise err
