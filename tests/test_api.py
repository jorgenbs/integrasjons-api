import json
import unittest
from unittest import mock
from django.test import RequestFactory
from django.conf import settings
from api import views, middleware
from unittest.mock import MagicMock, patch
from clients.fagsystem import Fagsystem

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
            return self.middleware.process_exception(e), None

    @mock.patch('api.services.fagsystem.opprett_kunde')
    @mock.patch('api.services.fagsystem.opprett_avtale')
    @mock.patch('api.services.send_email')
    def test_ok_response(self, send_email, opprett_avtale, opprett_kunde):
        # mock
        request = self.factory.post(path='/avtale')
        opprett_kunde.return_value = '2222'
        opprett_avtale.return_value = '3333'
        send_email.return_value = 'avtale sendt'

        # make request
        response, response_json = self.process_request(request)


        # assert 200 OK
        self.assertEquals(response.status_code, 200, 'OK')

        # assert json body
        self.assertAlmostEquals(response_json.get('avtalenummer'), '3333')
        self.assertAlmostEquals(response_json.get('status'), 'avtale sendt')

    def test_503_if_service_unavailable(self):
        # mock, but let fagsystem attempt request to nowhere
        request = self.factory.post(path='/avtale')

        # make request
        response, response_json = self.process_request(request)
        self.assertEquals(response.status_code, 503)

if __name__ == '__main__':
    unittest.main()
