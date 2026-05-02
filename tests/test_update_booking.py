import allure
import pytest
from routes.booking_routes import put_booking_request, patch_booking_request
from checkers.booking_checkers import check_booking_data, check_status_code, check_field


pytestmark=[allure.feature("Booking")]


@allure.story("PUT /booking/{id}")
@allure.step('fully update booking with valid token')
def test_put_booking_valid_token(valid_booking_id_with_creation_and_deletion, valid_booking_data_to_change):
    booking_data, auth_token = valid_booking_id_with_creation_and_deletion

    request_body = valid_booking_data_to_change

    response = put_booking_request(auth_token=auth_token, request_body=request_body, booking_id=booking_data["bookingid"])

    check_status_code(response, 200)
    check_booking_data(actual=response.json(), expected=request_body)


@allure.story("PUT /booking/{id}")
@allure.step('fully update booking with invalid token')
def test_put_booking_invalid_token(valid_booking_id_with_creation_and_deletion, valid_booking_data_to_change):
    booking_data, auth_token = valid_booking_id_with_creation_and_deletion

    request_body = valid_booking_data_to_change
    auth_token = '111'

    response = put_booking_request(auth_token=auth_token, request_body=request_body, booking_id=booking_data["bookingid"])

    check_status_code(response, 403)


@allure.story("PUT /booking/{id}")
@allure.step('fully update booking with invalid booking id')
@pytest.mark.parametrize('invalid_id', ['-1', 'asdfgh', ' ', '!'])
def test_put_booking_invalid_bookingid(valid_booking_data_to_change, auth_token, invalid_id):
    request_body = valid_booking_data_to_change
    bookingid = invalid_id

    response = put_booking_request(auth_token=auth_token, request_body=request_body, booking_id=bookingid)

    check_status_code(response, 405)


@allure.story("PUT /booking/{id}")
@allure.step('fully update booking with not existing booking id')
def test_put_booking_not_existing_bookingid(create_booking_and_delete, valid_booking_data_to_change, auth_token):
    request_body = valid_booking_data_to_change

    response = put_booking_request(auth_token=auth_token, request_body=request_body, booking_id=create_booking_and_delete)

    check_status_code(response, 405)


@allure.story("PATCH /booking/{id}")
@allure.step('partially update booking with valid data')
@pytest.mark.parametrize(
    'field_to_change, value_to_change',
    [
        ('firstname', 'new_name'),
        ('lastname', 'new_surname'),
        ('totalprice', 3010),
        ('depositpaid', False),
        ('additionalneeds', 'lunch')
    ]
)
def test_patch_booking_valid_data(valid_booking_id_with_creation_and_deletion, field_to_change, value_to_change):
    booking_data, auth_token = valid_booking_id_with_creation_and_deletion
    request_body={
        field_to_change: value_to_change
    }

    response = patch_booking_request(auth_token=auth_token, request_body=request_body, booking_id=booking_data["bookingid"])

    check_status_code(response, 200)
    check_field(response.json()[field_to_change], value_to_change)


@allure.story("PATCH /booking/{id}")
@allure.step('update bookingdates with valid data')
@pytest.mark.parametrize(
    'field_to_change, value_to_change',
    [
        ('checkin', '2011-01-01'),
        ('checkout', '2012-01-01')
    ]
)
def test_patch_bookingdates(valid_booking_id_with_creation_and_deletion, field_to_change, value_to_change, valid_booking_data_to_change):
    booking_data, auth_token = valid_booking_id_with_creation_and_deletion
    bookingdates = valid_booking_data_to_change["bookingdates"]
    request_body = {
        "bookingdates" : {
            "checkin":bookingdates["checkin"],
            "checkout":bookingdates["checkout"]
        }
    }
    request_body["bookingdates"][field_to_change] = value_to_change

    response = patch_booking_request(auth_token=auth_token, request_body=request_body, booking_id=booking_data["bookingid"])

    check_status_code(response, 200)
    check_field(response.json()["bookingdates"][field_to_change], value_to_change)
