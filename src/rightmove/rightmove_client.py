import requests
import logging

log = logging.getLogger()

BASE_URL = "https://www.rightmove.co.uk/"
PARAMS = {}

class RightMoveClient:
    def __init__self(self):
        return

    def get(self, endpoint, params={}) -> requests.Response:
        r = requests.get(endpoint, params)
        log.debug("Request url: %s", r.request.url)
        log.debug("Response status code: %s", r.status_code)
        return r;

    def get_properties_for_sale(self, params) -> requests.Response:
        return self.get(BASE_URL + "property-for-sale/find.html", params)
