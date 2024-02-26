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
        'pages': pages
    }


def search_result(request):
    
        if "searched_item" in request.GET:
            searched_term = request.GET["searched_item"]

            news = NewsArticle.objects.filter(Q(title__icontains=searched_term) | Q(category__icontains=searched_term) | Q(author__icontains=searched_term))
            blogs = Blog.objects.filter(Q(title__icontains=searched_term) | Q(category__icontains=searched_term) | Q(author__icontains=searched_term))
            jobs = Job.objects.filter(Q(job_title__icontains=searched_term) | Q(job_type__icontains=searched_term) | Q(Status__icontains=searched_term), Status='Active')
            gallery = GalleryImage.objects.filter(Q(title__icontains=searched_term) | Q(category__icontains=searched_term))
            documents = Document.objects.filter(Q(title__icontains=searched_term) | Q(category__icontains=searched_term))
            events = Event.objects.filter(Q(title__icontains=searched_term) | Q(location__icontains=searched_term))
            
            if news.count() == 0 and blogs.count() == 0 and jobs.count() == 0 and gallery.count() == 0 and documents.count() == 0 and events.count() == 0:
                return  {'no_result':True}
            
            return  { 
                "news_articles": news,
                "blogs": blogs, 
                "images": gallery, 
                "jobs": jobs, 
                "documents": documents, 
                "events": events, 
                "term": searched_term,
            }
        
        else:
            return  {'no_result':True}
