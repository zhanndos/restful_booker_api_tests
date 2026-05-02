import pytest
import allure
from routes.booking_routes import create_booking_request
from checkers.booking_checkers import check_booking_data, check_status_code


pytestmark=[allure.feature("Booking")]


@allure.story("POST /booking")
@allure.step('create booking with valid data')
def test_create_booking_with_valid_data(valid_booking_data):
    request_body = valid_booking_data

    response = create_booking_request(request_body=request_body)

    check_status_code(response, 200) 
    check_booking_data(response.json()["booking"], valid_booking_data)
    assert response.json()["bookingid"] is not None


@allure.story("POST /booking")
@allure.step('create booking with no required fields')
@pytest.mark.parametrize('field_to_miss', ['firstname', 'lastname', 'totalprice', 'depositpaid','bookingdates'])
def test_create_booking_without_required_fields(valid_booking_data, field_to_miss):
    request_body = valid_booking_data
    del request_body[field_to_miss]

    response = create_booking_request(request_body=request_body)

    check_status_code(response, 500)


@allure.story("POST /booking")
@allure.step('create booking without additionalneeds')
@pytest.mark.xfail(reason="Bug: additionalneeds is not required, API returns 200 instead of 500")
def test_create_booking_without_additionalneeds(valid_booking_data):
    request_body = valid_booking_data
    del request_body["additionalneeds"]

    response = create_booking_request(request_body=request_body)

    check_status_code(response, 500)


@allure.story("POST /booking")
@allure.step('create booking with invalid types in firstname and lastname')
@pytest.mark.parametrize('field_to_change', ['firstname', 'lastname'])
@pytest.mark.parametrize('invalid_type', [1,1.1, True, (), [], {}])
def test_create_booking_invalid_names(valid_booking_data, field_to_change, invalid_type):
    request_body = valid_booking_data
    request_body[field_to_change] = invalid_type

    response = create_booking_request(request_body=request_body)

    check_status_code(response, 500)


@allure.story("POST /booking")
@allure.step('create booking with invalid type in additionalneeds')
@pytest.mark.xfail(reason="Bug: additionalneeds accepts any type, should return 500")
@pytest.mark.parametrize('invalid_type', [1, 1.1, True, (), [], {}])
def test_create_booking_invalid_additionalneeds_type(valid_booking_data, invalid_type):
    request_body = valid_booking_data
    request_body['additionalneeds'] = invalid_type

    response = create_booking_request(request_body=request_body)

    check_status_code(response, 500)


@allure.story("POST /booking")
@allure.step('create booking with invalid type in totalprice')
@pytest.mark.xfail(reason="Bug: totalprice accepts any type, should return 500")
@pytest.mark.parametrize('invalid_type', [-1, True, (), [], {}, 'abc'])
def test_create_booking_invalid_totalprice_type(valid_booking_data, invalid_type):
    request_body = valid_booking_data
    request_body["totalprice"] = invalid_type

    response = create_booking_request(request_body=request_body)

    check_status_code(response, 500)


@allure.story("POST /booking")
@allure.step('create booking with invalid type in depositpaid')
@pytest.mark.xfail(reason="Bug: depositpaid accepts any type, should return 500")
@pytest.mark.parametrize('invalid_type', [-1, (), [], {}, 'abc'])
def test_create_booking_invalid_depositpaid_type(valid_booking_data, invalid_type):
    request_body = valid_booking_data
    request_body["depositpaid"] = invalid_type

    response = create_booking_request(request_body=request_body)

    check_status_code(response, 500)


@allure.story("POST /booking")
@allure.step('create booking with invalid type in bookingdates')
@pytest.mark.xfail(reason="Bug: bookingdates accepts any type, should return 500")
@pytest.mark.parametrize('field_to_change', ['checkin', 'checkout'])
@pytest.mark.parametrize('invalid_type', [1, 1.1, True, (), [], {}, 'abc'])
def test_create_booking_invalid_bookingdates_type(valid_booking_data, field_to_change, invalid_type):
    request_body = valid_booking_data
    request_body["bookingdates"][field_to_change] = invalid_type

    response = create_booking_request(request_body=request_body)
    bookingdates = response.json()["booking"]["bookingdates"]

    check_status_code(response, 500)
