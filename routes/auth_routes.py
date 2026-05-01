import allure
import requests
from config import BASE_URL

CREATE_TOKEN_AUTH_ROUTE = "/auth"

@allure.step("Post request to create token")
def login_request(request_body):
    response = requests.request(
        method="POST",
        url = BASE_URL + CREATE_TOKEN_AUTH_ROUTE,
        json=request_body
    )

    return response 
