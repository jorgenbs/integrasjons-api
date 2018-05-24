from django.views.decorators.csrf import csrf_exempt
from django import http
from django.views.decorators.http import require_POST

from . import services


@csrf_exempt
#@require_POST
def avtale(request):
    avtalenummer, status = services.create_customer({
        'foo': 'bar'
    })

    return http.JsonResponse(status=200, data={
        avtalenummer: avtalenummer,
        status: status
    })