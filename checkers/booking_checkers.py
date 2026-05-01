
def check_status_code(response, expected_status_code):
    assert response.status_code == expected_status_code


def check_booking_data(actual, expected):
    assert actual["firstname"] == expected["firstname"]
    assert actual["lastname"] == expected["lastname"]
    assert actual["totalprice"] == expected["totalprice"]
    assert actual["depositpaid"] == expected["depositpaid"]
    assert actual["additionalneeds"] == expected["additionalneeds"]
    assert actual["bookingdates"]["checkin"] == expected["bookingdates"]["checkin"]
    assert actual["bookingdates"]["checkout"] == expected["bookingdates"]["checkout"]

def check_field(actual, expected):
    assert actual == expected