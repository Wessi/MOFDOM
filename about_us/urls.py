from django.urls import path
from .views import *  # Import the faqs_api view

urlpatterns = [
    path('about/', about, name='about'),
    path('bureau_structure/', bureau_structure, name='bureau_structure'),
]

