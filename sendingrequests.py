import requests
import configurations
import data

def new_order():
    return requests.post(configurations.URL_SERVICE + configurations.CREATE_ORDER_PATH,
           json=data.order_body)


def order_info(track_number):
    return requests.get(configurations.URL_SERVICE + configurations.GET_ORDER_INFO,
           params={"t": track_number})