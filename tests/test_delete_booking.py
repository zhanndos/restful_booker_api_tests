import allure
import pytest
from routes.booking_routes import delete_booking_request
from checkers.booking_checkers import check_status_code


pytestmark=[allure.feature("Booking")]


@allure.story("DELETE /booking/{id}")
@allure.step('delete existing booking')
@pytest.mark.xfail(reason="Bug: DELETE returns 201 Created instead of 200 OK")
def test_delete_existing_booking(create_booking_valid_data, auth_token):
    booking_data = create_booking_valid_data

    response = delete_booking_request(auth_token=auth_token, booking_id=booking_data["bookingid"])

    check_status_code(response, 200)


@allure.story("DELETE /booking/{id}")
@allure.step('delete not existing booking')
def test_delete_not_existing_booking(create_booking_and_delete, auth_token):
    booking_id = create_booking_and_delete

    response = delete_booking_request(auth_token=auth_token, booking_id=booking_id)

    check_status_code(response, 405)


@allure.story("DELETE /booking/{id}")
@allure.step("delete booking by invalid id")
@pytest.mark.parametrize('booking_id', ['-1', 'a', '!', ' '])
def test_delete_booking_by_invalid_id(booking_id, auth_token):
    response = delete_booking_request(auth_token=auth_token, booking_id=booking_id)

    check_status_code(response, 405)


@allure.story("DELETE /booking/{id}")
@allure.step('delete booking with invalid auth_token')
@pytest.mark.parametrize('token', ['!', ' ', '-1'])
def test_delete_booking_invalid_token(create_booking_valid_data, token):
    booking_data = create_booking_valid_data

    response = delete_booking_request(auth_token=token, booking_id=booking_data["bookingid"])

    check_status_code(response, 403)
