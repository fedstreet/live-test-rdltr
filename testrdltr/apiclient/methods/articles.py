from __future__ import annotations
from requests import Response
from typing import List

from testrdltr.apiclient.methods.base import AuthenticatedRequest
from testrdltr.apiclient.loggingproxy import get, post, delete
from testrdltr.config import testconfig


class ArticlesGet(AuthenticatedRequest):
    def __init__(self):
        super().__init__()
        self.api_url = testconfig.get_base_api_url() + "/articles"

    def request_articles(self) -> ArticlesGetResponse:
        response = get(self.api_url, headers=self.headers)
        return ArticlesGetResponse(response)


class ArticlesPost(AuthenticatedRequest):
    def __init__(self, fill_default_values=False):
        super().__init__()
        self.api_url = testconfig.get_base_api_url() + "/articles"
        self.data = {}
        self.default_category_id = 1
        if fill_default_values:
            self.set_category_id(self.default_category_id)
            self.set_tags([])

    def set_article_url(self, url: str) -> ArticlesPost:
        self.data["url"] = url
        return self

    def set_category_id(self, category_id: int) -> ArticlesPost:
        self.data["category_id"] = category_id
        return self

    def set_tags(self, tags: List[str]) -> ArticlesPost:
        self.data["tags"] = tags
        return self

    def create_article(self) -> ArticlesPostResponse:
        response = post(self.api_url, headers=self.headers, json=self.data)
        return ArticlesPostResponse(response)


class ArticlesDelete(AuthenticatedRequest):
    def __init__(self):
        super().__init__()
        self.api_url_format = testconfig.get_base_api_url() + "/articles/{}"

    def delete(self, article_id: int) -> Response:
        response = delete(self.api_url_format.format(article_id), headers=self.headers)
        assert response.status_code == 204, "Article #{} deleted successfully".format(article_id)
        return response

    def delete_all(self, article_ids: List[int]):
        for article_id in article_ids:
            self.delete(article_id)


class ArticlesGetResponse(object):
    def __init__(self, response: Response):
        assert isinstance(response, Response), "Response should be a Response object"
        self.__response = response

    def assert_is_ok(self):
        assert self.__response.status_code == 200, "Request result should be OK"

    def get_pagination_page(self):
        return self.__response.json()["pagination"]["page"]

    def get_data(self) -> List[dict]:
        return self.__response.json()["data"]

    def get_all_ids(self):
        return [article["id"] for article in self.get_data()]


class ArticlesPostResponse(object):
    def __init__(self, response: Response):
        assert isinstance(response, Response), "Response should be a Response object"
        self.__response = response

    def get_status_code(self):
        return self.__response.status_code

    def get_status(self):
        return self.__response.json()["status"]

    def assert_created_successfully(self):
        assert self.get_status_code() == 201, "Response code should be CREATED"
        assert self.get_status() == "success", "Status in JSON should be 'success'"
