from requests import Response

from testrdltr.config import testconfig
from testrdltr.apiclient.loggingproxy import post

import allure

class AuthLoginResponse:
    def __init__(self, response: Response):
        assert isinstance(response, Response), "Should be initialized with a Response object"
        self.__response = response

    def assert_is_ok(self):
        assert self.__response.status_code == 200, "Status code should be 200"

    def get_auth_token(self):
        return str(self.__response.json()["auth_token"])


class AuthLoginPost:
    def __init__(self):
        self.api_url = testconfig.get_base_api_url() + "/auth/login"

    @allure.step
    def request_login(self, email: str, password: str) -> AuthLoginResponse:
        login_response = post(self.api_url, json={"email": "a@a.a", "password": "userpass"})
        return AuthLoginResponse(login_response)
