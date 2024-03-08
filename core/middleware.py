from core.models import Visitors
from django.middleware.security import SecurityMiddleware


class VisitorMiddleware:
    def __init__(self, get_response):
        # One-time configuration and initialization.
        self.get_response = get_response
       
    def __call__(self, request):
        non =['media','static','admin','dashboard','documents','jsi18n', 'i18n', 'filer', 'translator']
        main = (request.path.split('/'))
        if not main[1] in non:
            Visitors.objects.create()
        response = self.get_response(request)
        return response
