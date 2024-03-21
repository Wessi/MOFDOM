
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from core.views import index, search, EventListPage, GalleryImagePage, GalleryVideoPage, Contact
from django.views.i18n import JavaScriptCatalog
from django.utils.translation import gettext_lazy as _
from django.conf.urls.i18n import i18n_patterns

admin.site.site_header = 'Super Administrator'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),

    # Include your app-specific URLs here
    path('news/', include('news.urls')),
    path('blogs/', include('blogs.urls')),
    path('accounts/', include('accounts.urls')),
    path('about-us/', include('about_us.urls')),
    path('suppliers/', include('suppliers.urls')),
    path('vacancies/', include('vacancies.urls')),
    path('documents/', include('documents.urls')),  
    path('dashboard/', include('dashboard.urls')),# URLs for internal dashboards
    path('taskmanager/', include('task_manager.urls')),
    

    # direct urls
    path('search/', search, name='search'), #header search functionality
    path("contact-us/",Contact.as_view(), name="contact_us"),
    path('events/', EventListPage.as_view(), name='events_list'),
    path('gallery-images/', GalleryImagePage.as_view(), name='gallery_images'),
    path('gallery-videos/', GalleryVideoPage.as_view(), name='gallery_videos'),
    path('bids/', TemplateView.as_view(template_name = "front/bid.html"), name='bid'),
    path('services/', TemplateView.as_view(template_name = "front/services.html"), name='services'),
    
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    path('i18n/', include('django.conf.urls.i18n')),
    
    path('filer/', include('filer.urls')),
    path('', include('cms.urls')),

]
urlpatterns = [
    *i18n_patterns(*urlpatterns, prefix_default_language=False),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

