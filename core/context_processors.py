from .models import Settings, Pages
from dashboard.models import QuickLink
from visit_counter.models import UserVisit

def stgs(request):
    quick_links = QuickLink.objects.all()
    pages = Pages.objects.first()
    print(Pages.objects.all())
    return {
        'quick_links': quick_links,  # Include footer data in context
        'stg':Settings.objects.first(),
        'pages': pages,
        'visitors':UserVisit.objects.count()
    }

