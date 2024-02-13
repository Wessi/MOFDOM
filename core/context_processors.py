from django.contrib.auth.models import AnonymousUser
# from accounts.utils import staff_is_active
# def user_permissions(request):
#     if request.user.is_authenticated and staff_is_active ( request.user ):
#         return { 'user_perms':request.user.get_all_permissions()}
#     else:
#         return { 'user_perms':[]}
from news.models import NewsArticle

def recent_news_mega(request):
    recent_news = NewsArticle.objects.order_by('-created_at')
    recent_news  = recent_news[:4] if recent_news else recent_news 
    return {'recent_news_mega':recent_news}
    
