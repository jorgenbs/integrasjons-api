import settings
from clients.api_client import ApiClient


class Brevtjeneste(ApiClient):
    """
        Har antatt at Brevtjeneste også er et slags REST API
    """
    def __init__(self):
        super(Brevtjeneste, self).__init__(settings.BREVTJENESTE_ENDPOINT)

    def send_mail(self, to, message):
        body, status = self.post(self.ENDPOINT + '/send', {
            'to': to,
            'message': message,
        })

        if status >= 300:
            raise Exception("kunne ikke sende mail")

        return body.status

