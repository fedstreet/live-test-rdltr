from pytest import fixture

from testrdltr.setup import pageserver
from testrdltr.apiclient.loggingproxy import post


@fixture(scope="session")
def auth_token():
    login_url = "http://localhost:5000/api/auth/login"
    login_response = post(login_url, json={"email": "a@a.a", "password": "userpass"})
    assert login_response.status_code == 200
    token = login_response.json()["auth_token"]
    print(f"Received Auth token: {token}")
    return f"Bearer {token}"


@fixture(scope="session", autouse=True)
def stub_server():
    pageserver.start_server()
    yield
    pageserver.stop_server()
