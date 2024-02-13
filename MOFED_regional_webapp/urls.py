
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from dashboard.views import index
from core.views import Contact
admin.site.site_header = 'Super Adminstrator'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', TemplateView.as_view(template_name='base.html')),
    path('', index, name="index"),
   
    
    # Include your app-specific URLs here
    path('news/', include('news.urls')),
    path('accounts/', include('accounts.urls')),
    path('about_us/', include('about_us.urls')),
    path('dashboard/', include('dashboard.urls')),# Replace 'news.urls' with your actual news app URLs
    path('documents/', include('documents.urls')),  # Replace 'documents.urls' with your actual documents app URLs
    path('taskmanager/', include('task_manager.urls')),
    path('suppliers/', include('suppliers.urls')),
    path('vacancies/', include('vacancies.urls')),
    path('blogs/', include('blogs.urls')),
    
    
    #path('neews/',TemplateView.as_view(template_name = 'front/news.html'), name="news"),
    #path('doocuments/',TemplateView.as_view(template_name = 'front/docs.html'), name="docs"),    
    path('hoome-2/',TemplateView.as_view(template_name = 'front/home-2.html'), name="home_2"),
    path('aabout/', TemplateView.as_view(template_name = 'front/about.html'), name='about'),
    path('structure/',TemplateView.as_view(template_name = 'front/structure.html'), name="structure"),
    path('structure/',TemplateView.as_view(template_name = 'front/structure.html'), name="structure"),
    path('bloog/',TemplateView.as_view(template_name = 'front/blog.html'), name="blog"),
    path('gallery/',TemplateView.as_view(template_name = 'front/gallery.html'), name="gallery"),
    path('vacancy/',TemplateView.as_view(template_name = 'front/vacancy.html'), name="vacancy"),
    #path('eveents/',TemplateView.as_view(template_name = 'front/event.html'), name="events"),
    path("contact-us/",Contact.as_view(), name="contact_us"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
