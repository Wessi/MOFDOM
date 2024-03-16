
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from dashboard.views import index, search
from core.context_processors import search_result
from core.views import Contact
from django.views.i18n import JavaScriptCatalog
from django.utils.translation import gettext_lazy as _
from django.conf.urls.i18n import i18n_patterns


admin.site.site_header = 'Super Adminstrator'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),

    # Include your app-specific URLs here
    path('news/', include('news.urls')),
    path('accounts/', include('accounts.urls')),
    path('about-us/', include('about_us.urls')),
    path('dashboard/', include('dashboard.urls')),# Replace 'news.urls' with your actual news app URLs
    path('documents/', include('documents.urls')),  # Replace 'documents.urls' with your actual documents app URLs
    path('taskmanager/', include('task_manager.urls')),
    path('suppliers/', include('suppliers.urls')),
    path('vacancies/', include('vacancies.urls')),
    path('blogs/', include('blogs.urls')),

    # direct pages
    path('search/', search, name='search'), #header search functionality
    path("contact-us/",Contact.as_view(), name="contact_us"),
    path('services/', TemplateView.as_view(template_name = "front/services.html"), name='services'),
    path('bids/', TemplateView.as_view(template_name = "front/bid.html"), name='bid'),
    
    
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    path('i18n/', include('django.conf.urls.i18n')),
    
    path('filer/', include('filer.urls')),
    path('translator/', include('rosetta.urls')),
    path('', include('cms.urls')),

]
urlpatterns = [
    *i18n_patterns(*urlpatterns, prefix_default_language=False),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

