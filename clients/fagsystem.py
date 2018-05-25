import settings
from clients.api_client import ApiClient


class Fagsystem(ApiClient):

    def __init__(self):
        super(Fagsystem, self).__init__(settings.FAGSYSTEM_ENDPOINT)

    def opprett_kunde(self, kunde_info) -> str:
        body, status = self.post(self.ENDPOINT + '/kunder', kunde_info)

        if status >= 300:
            raise Exception('asdf')

        return body.kundeNr

    def opprett_avtale(self, kunde_nummer: int) -> str:
        body, status = self.post(self.ENDPOINT + '/avtaler', {'kundeNr': kunde_nummer})

        if status >= 300:
            raise Exception('asdf')

        return body.avtalenummer
