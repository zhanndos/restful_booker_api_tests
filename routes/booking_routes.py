import allure
import requests
from config import BASE_URL

GET_POST_BOOKINGS_ROUTE = "/booking"
GET_PUT_PATCH_DELETE_BOOKING_ROUTE = "/booking/{id}"


@allure.step("request to get bookings")
def get_bookings_request():
    response = requests.request(
        method="GET",
        url = BASE_URL + GET_POST_BOOKINGS_ROUTE,
    )

    return response 


@allure.step("request to get booking by id")
def get_booking_by_id_request(booking_id):
    response = requests.request(
        method="GET",
        url = (BASE_URL + GET_PUT_PATCH_DELETE_BOOKING_ROUTE).format(id=booking_id)
    )

    return response 


@allure.step("request to create booking")
def create_booking_request(request_body):
    response = requests.request(
        method="POST",
        url = BASE_URL + GET_POST_BOOKINGS_ROUTE,
        json=request_body
    )

    return response


@allure.step("request to fully update booking")
def put_booking_request(auth_token, request_body, booking_id):
    headers ={'Cookie': f"token={auth_token}"}
    response = requests.request(
        method="PUT",
        url = (BASE_URL + GET_PUT_PATCH_DELETE_BOOKING_ROUTE).format(id=booking_id),
        json=request_body,
        headers=headers
    )

    return response


@allure.step("request to partially update booking")
def patch_booking_request(auth_token, request_body, booking_id):
    headers ={'Cookie': f"token={auth_token}"}
    response = requests.request(
        method="PATCH",
        url = (BASE_URL + GET_PUT_PATCH_DELETE_BOOKING_ROUTE).format(id=booking_id),
        json=request_body,
        headers=headers
    )

    return response



@allure.step("request to delete booking")
def delete_booking_request(auth_token, booking_id):
    headers ={'Cookie': f"token={auth_token}"}
    response = requests.request(
        method="DELETE",
        url = (BASE_URL + GET_PUT_PATCH_DELETE_BOOKING_ROUTE).format(id=booking_id),
        headers=headers
    )

    return response
