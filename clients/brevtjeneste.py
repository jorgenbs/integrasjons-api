import settings
from api.exceptions import ServiceNotAvailableException
from clients.api_client import ApiClient


class Brevtjeneste(ApiClient):
    """
        Har antatt at Brevtjeneste også er et slags REST API
    """
    def __init__(self):
        super(Brevtjeneste, self).__init__(settings.BREVTJENESTE_ENDPOINT)

    def send_mail(self, to, message) -> bool:
        body, status = self.post(self.ENDPOINT + '/send', {
            'to': to,
            'message': message,
        })

        if status >= 300:
            raise ServiceNotAvailableException("kunne ikke sende mail")

        return True

