import pytest
import allure
from config import USER, PASSWORD
from routes.auth_routes import login_request

@allure.step("Login with valid data")
def test_valid_data(auth_token):
    token = auth_token

    assert token != None

@allure.step("Login with invalid data")
@pytest.mark.parametrize('field_to_change', ['username', 'password'])
def test_invalid_data(field_to_change):
    request_body = {
        "username": USER,
        "password": PASSWORD
    }
    request_body[field_to_change] = "random_str"

    response = login_request(request_body=request_body)

    assert response.status_code == 200 # это баг api, должно возвращаться 401
    assert response.json()["reason"] == "Bad credentials"


@allure.step("Login without required fields")
@pytest.mark.parametrize('field_to_miss', ['username', 'password'])
def test_missing_required_field(field_to_miss):
    request_body = {
        "username": USER,
        "password": PASSWORD
    }
    del request_body[field_to_miss]

    response = login_request(request_body=request_body)

    assert response.status_code == 200 # это баг api, должно возвращаться 401
    assert response.json()["reason"] == "Bad credentials"
