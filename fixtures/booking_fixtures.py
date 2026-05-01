import pytest
from routes.booking_routes import create_booking_request, delete_booking_request
from config import USER, PASSWORD


@pytest.fixture
def valid_booking_data():
    return {
        "firstname" : "Vasya",
        "lastname" : "Pupkin",
        "totalprice" : 100,
        "depositpaid" : True,
        "bookingdates" : {
            "checkin" : "2026-01-01",
            "checkout" : "2027-01-01"
        },
        "additionalneeds" : "dinner"
    }

@pytest.fixture
def create_booking_valid_data(valid_booking_data, auth_token):
    booking = create_booking_request(valid_booking_data)
    return booking.json()

@pytest.fixture
def valid_booking_id_with_creation_and_deletion(create_booking_valid_data, auth_token):
    booking = create_booking_valid_data
    booking_id = booking['bookingid']

    yield booking, auth_token

    delete_booking_request(auth_token=auth_token, booking_id=booking_id)

@pytest.fixture
def valid_booking_data_to_change():
    return {
        "firstname" : "Ivan",
        "lastname" : "Ivanov",
        "totalprice" : 200,
        "depositpaid" : True,
        "bookingdates" : {
            "checkin" : "2026-01-01",
            "checkout" : "2027-01-01"
        },
        "additionalneeds" : "lunch"
    }

@pytest.fixture
def create_booking_and_delete(create_booking_valid_data, auth_token):
    booking = create_booking_valid_data
    booking_id = booking['bookingid']
    delete_booking_request(auth_token=auth_token, booking_id=booking_id)
    yield booking_id



