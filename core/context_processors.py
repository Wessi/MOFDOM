from django.contrib.auth.models import AnonymousUser
# from accounts.utils import staff_is_active
# def user_permissions(request):
#     if request.user.is_authenticated and staff_is_active ( request.user ):
#         return { 'user_perms':request.user.get_all_permissions()}
#     else:
#         return { 'user_perms':[]}

from news.models import NewsArticle
from blogs.models import Blog
from vacancies.models import Job
from documents.models import Document
from dashboard.models import *      # GalleryImage, Event
from core.models import Settings, Pages
from django.db.models import Q
from core.models import Visitors

def recent_news_mega(request):
    recent_news = NewsArticle.objects.order_by('-created_at')
    recent_news  = recent_news[:4] if recent_news else recent_news 
    return {'recent_news_mega':recent_news}
    

def stgs(request):
    contact_info = ContactInfo.objects.first()
    quick_links = QuickLink.objects.all()
    
    pages = Pages.objects.first()
    return {
        'contact_info': contact_info,  # Include footer data in context
        'quick_links': quick_links,  # Include footer data in context
        'stg':Settings.objects.first(),
        'pages': pages,
        'visitors':Visitors.objects.count()
    }

