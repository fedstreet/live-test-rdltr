from pytest import fixture

from testrdltr.config import testconfig
from testrdltr.setup import pageserver
from testrdltr.apiclient.methods.auth_login import AuthLoginPost
from testrdltr.apiclient.methods.articles import ArticlesGet, ArticlesDelete


@fixture(scope="session")
def auth_token():
    response = AuthLoginPost().request_login(
        testconfig.get_user_email(),
        testconfig.get_user_pasword())
    response.assert_is_ok()
    token = response.get_auth_token()
    print(f"Received Auth token: {token}")
    return f"Bearer {token}"


@fixture(scope="session", autouse=True)
def stub_server():
    pageserver.start_server()
    yield
    pageserver.stop_server()


@fixture(scope="session", autouse=True)
def delete_all_articles(auth_token):
    print("Removing all articles...")
    articles = ArticlesGet().set_auth(auth_token).request_articles()
    ArticlesDelete().set_auth(auth_token).delete_all(articles.get_all_ids())
