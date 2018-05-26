from django import http
from django.utils.deprecation import MiddlewareMixin

from api import exceptions


class ViewExceptionMiddleware(MiddlewareMixin):

    def process_exception(self, exception):
        error = exception.args[0] if len(exception.args) else 'Unknown'

        if isinstance(exception, exceptions.ServiceNotAvailableException):
            return http.JsonResponse(status=503, data={
                'error': error,
            })

        if isinstance(exception, exceptions.CouldNotUpdateAvtaleException):
            return http.JsonResponse(status=200, data={
                'avtalenummer': exception.args[0],
                'status' : 'Avtale sendt, men vi klarte ikke oppdatere databasen vår. Kontakt support',
            })

        # unhandled
        return http.JsonResponse(status=500, data={
            'error': error,
        })

