
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from dashboard.views import index
from core.views import Contact
from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import JavaScriptCatalog
from django.utils.translation import gettext_lazy as _


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
    
    
    path('structure/',TemplateView.as_view(template_name = 'front/structure.html'), name="structure"),
    path('structure/',TemplateView.as_view(template_name = 'front/structure.html'), name="structure"),
    path('bloog/',TemplateView.as_view(template_name = 'front/blog.html'), name="blog"),
    path('gallery/',TemplateView.as_view(template_name = 'front/gallery.html'), name="gallery"),
    path('vacancy/',TemplateView.as_view(template_name = 'front/vacancy.html'), name="vacancy"),
    path("contact-us/",Contact.as_view(), name="contact_us"),
    path("privacy/", TemplateView.as_view(template_name = "front/privacy.html"), name="privacy_page"),

    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    path('i18n/', include('django.conf.urls.i18n')),
    
    path('filer/', include('filer.urls')),
    path('translator/', include('rosetta.urls')),
    path('', include('cms.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns(
    path(_('home/'), index, name="home"),
    path(_('news/'), include('news.urls')),
    # path(_('admin/'), include(admin.site.urls)),
    
   #your urls
)