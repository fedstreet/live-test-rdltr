from requests import get, post


def get_auth_token():
    login_url = "http://localhost:5000/api/auth/login"
    login_response = post(login_url, json={"email": "a@a.a", "password": "userpass"})
    assert login_response.status_code == 200
    return login_response.json()["auth_token"]


def test_articles_return_page_1():
    auth_token = get_auth_token()
    articles_url = "http://localhost:5000/api/articles"
    articles_response = get(articles_url, headers={"Authorization": f"Bearer {auth_token}"})
    assert articles_response.status_code == 200
    assert articles_response.json()["pagination"]["page"] == 1


def test_profile_returns_success_when_authenticated():
    auth_token = get_auth_token()
    url = "http://localhost:5000/api/auth/profile"
    response = get(url, headers={"Authorization": f"Bearer {auth_token}"})
    assert response.status_code == 200, "HTTP response Status code"
    assert response.json()["status"] == "success", "Profile status"
