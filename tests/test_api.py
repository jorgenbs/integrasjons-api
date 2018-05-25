import unittest
from unittest import mock
from django.test import RequestFactory
from django.conf import settings
from api import views
from unittest.mock import MagicMock, patch
from clients.fagsystem import Fagsystem

settings.configure()

class TestStringMethods(unittest.TestCase):

    #@mock.patch('api.services.fagsystem')
    def test_ok_response(self):
        factory = RequestFactory()
        request = factory.post(path='/avtale')

        with patch.object(Fagsystem, 'opprett_kunde', return_value='11111'):
            response = views.avtale(request)


    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
