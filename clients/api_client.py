import json

import requests

from api import exceptions


class ApiClient:
    """ Generic class for REST clients """

    def __init__(self, endpoint):
        self.ENDPOINT = endpoint

    def _request(self, func, path, payload=None) -> (dict, int):
        try:
            response = func("{}{}".format(self.ENDPOINT, path))
            response_json = json.loads(response.content.decode())

            return response_json, response.status_code
        except:
            # return 503
            raise exceptions.ServiceNotAvailableException()

    def get(self, path):
        return self._request(requests.get, path)

    def post(self, path, payload):
        return self._request(requests.post, path, payload)

    def put(self, path, payload):
        return self._request(requests.put, path, payload)