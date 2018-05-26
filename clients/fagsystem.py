import settings
from api.exceptions import ServiceNotAvailableException, CouldNotUpdateAvtaleException, CouldNotCreateCustomerException, \
    CouldNotCreateAvtaleException
from clients.api_client import ApiClient


class Fagsystem(ApiClient):

    def __init__(self):
        super(Fagsystem, self).__init__(settings.FAGSYSTEM_ENDPOINT)

    def opprett_kunde(self, kunde_info) -> (str, str):
        body, status = self.post(self.ENDPOINT + '/kunder', kunde_info)

        if status >= 300:
            raise CouldNotCreateCustomerException()

        return body.kundeNr, body.kundeMail

    def opprett_avtale(self, kunde_nummer: str) -> str:
        body, status = self.post(self.ENDPOINT + '/avtaler', {
            'kundeNr': kunde_nummer
        })

        if status >= 300:
            raise CouldNotCreateAvtaleException()

        return body.avtalenummer

    def oppdater_avtale(self, avtale_nummer: str, status: str) -> bool:
        body, status = self.put("{}/avtaler/{}".format(self.ENDPOINT, '/avtaler/', avtale_nummer), {
            'status': status,
        })

        if status >= 300:
            raise CouldNotUpdateAvtaleException(avtale_nummer)

        return True
