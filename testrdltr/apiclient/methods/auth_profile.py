from requests import Response

from testrdltr.apiclient.methods.base import AuthenticatedRequest
from testrdltr.config import testconfig
from testrdltr.apiclient.loggingproxy import get


class AuthProfileResponse:
    def __init__(self, response: Response):
        assert isinstance(response, Response), "Should be initialized with a Response object"
        self.__response = response

    def assert_is_ok(self):
        assert self.__response.status_code == 200, "Status code should be 200"

    def get_profile_status(self):
        return str(self.__response.json()["status"])


class AuthProfilePost(AuthenticatedRequest):
    def __init__(self):
        super().__init__()
        self.api_url = testconfig.get_base_api_url() + "/auth/profile"

    def request_profile(self) -> AuthProfileResponse:
        response = get(self.api_url, headers=self.headers)
        return AuthProfileResponse(response)
