import json
import requests
from rapidtables import print_table
from typing import Dict


def get(*args, **kwargs) -> requests.Response:
    return request_with_logging(requests.get, False, *args, **kwargs)


def post(*args, **kwargs) -> requests.Response:
    return request_with_logging(requests.post, True, *args, **kwargs)


def delete(*args, **kwargs) -> requests.Response:
    return request_with_logging(requests.delete, False, *args, **kwargs)


def request_with_logging(request_method, request_has_body, *args, **kwargs) -> requests.Response:
    print("===== Request data: =====")
    print(f"URL: {args[0]}")
    print_headers(kwargs.get("headers", {}))
    if request_has_body:
        print_request_body(**kwargs)
    try:
        response = request_method(*args, **kwargs)
        print("===== Response data: =====")
        print(f"HTTP code: {response.status_code}")
        print_headers(response.headers)
        print_response_body(response)
        return response
    except Exception as e:
        print("===== Request error: =====")
        print(f"Exception: {e!r}")
        raise e


def print_headers(headers: Dict[str, str]):
    headers_table = [{"Header": key, "Value": value} for key, value in headers.items()]
    print_table(headers_table)


def print_request_body(**kwargs):
    print("===== START Request body: =====")
    if "json" in kwargs:
        print_json(kwargs["json"])
    else:
        print("Body other than JSON is not yet supported!")

    print("===== END Request body: =====")


def print_response_body(response: requests.Response):
    print("===== START Response body: =====")
    try:
        print_json(response.json())
    except ValueError:
        if response.content:
            print(response.content.decode())
        else:
            print("<NO CONTENT>")

    print("===== END Response body: =====")


def print_json(json_data):
    print(json.dumps(json_data, sort_keys=True, indent=2))
