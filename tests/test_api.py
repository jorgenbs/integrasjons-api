import json
import unittest
from unittest import mock
from django.test import RequestFactory
from django.conf import settings
from api import views, middleware

settings.configure()


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.middleware = middleware.ViewExceptionMiddleware()

    def process_request(self, request):
        """
            helper method for making POST request to /avtale
            as well as running exceptions through middleware
        """
        try:
            response = views.avtale(request)
            response_json = json.loads(response.content.decode())
            return response, response_json
        except Exception as e:
            response = self.middleware.process_exception(e)
            try:
                response_json = json.loads(response.content.decode())
                return response, response_json
            except:
                return response, None

    @mock.patch('api.services.fagsystem.opprett_kunde')
    @mock.patch('api.services.fagsystem.opprett_avtale')
    @mock.patch('api.services.fagsystem.oppdater_avtale')
    @mock.patch('api.services.send_email')
    def test_ok_response(self, send_email, oppdater_avtale, opprett_avtale, opprett_kunde):
        # mock
        request = self.factory.post(path='/avtale')
        opprett_kunde.return_value = ('2222', 'mail@mail.com')
        opprett_avtale.return_value = '3333'
        oppdater_avtale.return_value = True
        send_email.return_value = 'avtale sendt'

        # make request
        response, response_json = self.process_request(request)


        # assert 200 OK
        self.assertEquals(response.status_code, 200, 'OK')

        # assert json body
        self.assertAlmostEquals(response_json.get('avtalenummer'), '3333', 'avtale nummer er riktig')
        self.assertAlmostEquals(response_json.get('status'), 'avtale sendt', 'status er riktig')

        # assert mail was sendt
        send_email.assert_called_with('mail@mail.com', '3333')

    def test_503_if_service_unavailable(self):
        # mock, but let fagsystem attempt request to nowhere
        request = self.factory.post(path='/avtale')

        # make request
        response, response_json = self.process_request(request)
        self.assertEquals(response.status_code, 503)

    @mock.patch('api.services.fagsystem.opprett_kunde')
    @mock.patch('api.services.fagsystem.opprett_avtale')
    @mock.patch('api.services.fagsystem.put')
    @mock.patch('api.services.send_email')
    def test_could_not_update_avtale(self, send_email, http_put, opprett_avtale, opprett_kunde):
        request = self.factory.post(path='/avtale')
        opprett_kunde.return_value = ('2222', 'mail@mail.com')
        opprett_avtale.return_value = '3333'
        send_email.return_value = 'avtale sendt'

        # Mock http  PUT to return with HTTP STATUS 400, thereby failing
        http_put.return_value = (True, 400)

        # make request
        response, response_json = self.process_request(request)

        self.assertAlmostEqual(response_json.get('status'), 'Avtale sendt, men vi klarte ikke oppdatere databasen vår. Kontakt support')

if __name__ == '__main__':
    unittest.main()
