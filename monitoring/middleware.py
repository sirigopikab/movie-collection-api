from django.db.models import F
from monitoring.models import RequestCount

EXCLUDED_PATHS = [
    "/request-count/",
    "/request-count/reset/"
]

class RequestCounterMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        # do not count monitoring APIs themselves
        if request.path not in EXCLUDED_PATHS:
            RequestCount.objects.filter(key="global").update(count=F("count") + 1)

        response = self.get_response(request)
        return response

