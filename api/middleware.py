from django import http
from django.utils.deprecation import MiddlewareMixin

from api import exceptions


class ViewExceptionMiddleware(MiddlewareMixin):

    @staticmethod
    def process_exception(self, exception):
        if isinstance(exception, exceptions.ServiceNotAvailableException):
            return http.HttpResponse(status=503)

        # unhandled
        return http.HttpResponse(status=500)