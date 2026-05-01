import pytest
from routes.auth_routes import login_request
from config import USER, PASSWORD

@pytest.fixture(scope="session")
def auth_token():
    request_body = {
        "username" : USER,
        "password" : PASSWORD
    }

    response = login_request(request_body=request_body)

    return response.json()["token"]

