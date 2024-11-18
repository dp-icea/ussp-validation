from api.utils.client.utm_client import UTMClientConfig
from requests import Request, Session, Response
from os import _Environ


class UsspClient(UTMClientConfig):
    def __init__(self, session: Session, set_env_vars: _Environ[str]):
        super().__init__()
        self.base_url = set_env_vars.get("USSP_URL")
        self.session = session

    def request_put_oir(self, oir_id: str, request_body) -> Response:
        req = Request("PUT", self.base_url + oir_id, data=request_body, headers={})
        prepped_req = self.session.prepare_request(req)

        try:
            return self.session.send(prepped_req)
        except Exception as err:
            raise err

    def request_get_oir(self, oir_id: str) -> Response:
        url = self.base_url + f"/uss/v1/operational_intents/${oir_id}"
        req = Request("GET", url, {}, {})
        prepped_req = self.session.prepare_request(req)

        try:
            return self.session.send(prepped_req)
        except Exception as err:
            raise err

    def request_put_flight_plans(self, flight_plan_id: str) -> Response:
        url = self.base_url + f"/flight_plans/${flight_plan_id}"
        body = {}

        req = Request("PUT", url, data=body, headers={})
        prepped_req = self.session.prepare_request(req)

        try:
            return self.session.send(prepped_req)

        except Exception as err:
            raise err