import pytest
import allure
from routes.booking_routes import get_bookings_request, get_booking_by_id_request
from checkers.booking_checkers import check_booking_data, check_status_code


@allure.step("get bookings")
def test_get_bookings():
    response = get_bookings_request()

    check_status_code(response, 200)
    assert isinstance(response.json(), list)
    
    
@allure.step("get booking by valid id")
def test_get_booking_by_valid_id(valid_booking_id_with_creation_and_deletion, valid_booking_data):
    booking_data, auth_token = valid_booking_id_with_creation_and_deletion

    response = get_booking_by_id_request(booking_data["bookingid"])

    check_status_code(response, 200)
    check_booking_data(response.json(), valid_booking_data) 
        

@allure.step("get booking by invalid id")
@pytest.mark.parametrize('booking_id', ['-1', 'a', '!', ' '])
def test_get_booking_by_invalid_id(booking_id):
    response = get_booking_by_id_request(booking_id=booking_id)

    check_status_code(response, 404)
