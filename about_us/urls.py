from django.urls import path
from .views import *  # Import the faqs_api view

urlpatterns = [
    path('about_us/', about_us, name='add_faq_api'),
    #path('about-us/edit/', about_us_edit, name='add_faq_api'),
    path('contact_us/', contact_us, name='add_faq_api'),
    path('our_structure/', our_structure, name='our_structure'),
    path('directories/', directories, name='our_directories'),
    path('directories_detail/', directories_detail, name='directories_detail'),
    path('about/', about, name='aboutt'),
    path('bureau_structure/', bureau_structure, name='bureau_structure'),
    
    
    

]

