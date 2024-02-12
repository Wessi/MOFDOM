from django.urls import path
from .views import *

urlpatterns = [
    path('blogs/', blog_list, name='blog_list'),
    # Other paths...
    path('blogs/<int:blog_id>/', blog_detail, name='blog_detail'),
    path('blogs/<int:blog_id>/comment/', add_comment, name='add_comment'),
    path('comments/<int:comment_id>/reply/', add_reply, name='add_reply'),  # New path
    path('add_blogs/',Blogs_add, name='add_blogs'),
    path('blogs_list/', blog_list_admin, name='blog_list_admin'),
    path('blog/<int:blog_id>/delete/', delete_blog, name='delete_blog'),
   
]
