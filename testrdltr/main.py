from requests import get, post

if __name__ == '__main__':
    login_url = "http://localhost:5000/api/auth/login"
    login_response = post(login_url, json={"email": "a@a.a", "password": "userpass"})
    assert login_response.status_code == 200
    auth_token = login_response.json()["auth_token"]

    articles_url = "http://localhost:5000/api/articles"
    articles_response = get(articles_url, headers={"Authorization": f"Bearer {auth_token}"})
    assert articles_response.status_code == 200
    assert articles_response.json()["pagination"]["page"] == 1
    print("OK")
