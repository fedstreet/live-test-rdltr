from pytest import mark, fixture

from testrdltr.apiclient.methods.articles import ArticlesPost


def test_create_article_with_non_existing_category(auth_token):
    # TODO
    raise NotImplementedError()


@mark.parametrize("article_url", [
    "http://localhost:8000/default_page.html",
    "http://127.0.0.1:8000/default_page.html",
    "http://[::1]:8000/default_page.html",
])
def test_create_article_with_valid_urls(auth_token, article_url):
    ArticlesPost().set_auth(auth_token).set_article_url(article_url).create_article().assert_created_successfully()


@fixture(params=[
    "http://localhost:8000/default_page.html",
    "http://127.0.0.1:8000/default_page.html",
    "http://[::1]:8000/default_page.html",
])
def valid_urls(request):
    return request.param


def test_create_article_with_valid_urls2(auth_token, valid_urls):
    ArticlesPost().set_auth(auth_token).set_article_url(valid_urls).create_article().assert_created_successfully()
