import sendingrequests


def track_number_of_order():
    track_number = sendingrequests.new_order()
    return track_number.json()["track"]


def test_track_order():
    track_number = track_number_of_order()
    get_response = sendingrequests.order_info(track_number)
    assert get_response.status_code == 200
# Емельянов Константин, 6 поток, Earth, Финальный проект