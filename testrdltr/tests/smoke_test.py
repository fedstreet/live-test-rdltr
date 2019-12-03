from testrdltr.setup import pageserver
from testrdltr.apiclient.methods.auth_profile import AuthProfilePost
from testrdltr.apiclient.methods.articles import ArticlesGet, ArticlesPost


def test_articles_return_page_1(auth_token):
    articles = ArticlesGet() \
        .set_auth(auth_token) \
        .request_articles()
    articles.assert_is_ok()
    assert articles.get_pagination_page() == 1, "Default page is 1"


def test_profile_returns_success_when_authenticated(auth_token):
    response = AuthProfilePost() \
        .set_auth(auth_token) \
        .request_profile()
    response.assert_is_ok()
    assert response.get_profile_status() == "success", "Profile status"


def test_add_article(auth_token):
    ArticlesPost(fill_default_values=True) \
        .set_auth(auth_token) \
        .set_article_url(pageserver.get_default_page_url()) \
        .create_article() \
        .assert_created_successfully()
