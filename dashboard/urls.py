from django.urls import path
from .views import *  # Import the faqs_api view

urlpatterns = [

    path('', admin_dashboard, name='admin_dashboard'),
    # path('panel/faq/add', add_FAQs, name='faq_add'),
    path('faq_add/', add_FAQs, name='faq_add'),#used

    path('panel/gallarie_image/add', add_gallarie_image, name='gallarie_add'),
    path('panel/footers/add', edit_footers, name='footers_add'),
    path('panel/sliders/add', add_sliders, name='footers_add'),
    path('privacy/', privacy_index, name='privacy_index'),
    path('add_gallary_back/', add_gallarie_image_back, name='add_gallary_back'),
    path('gallarie_all/', gallarie_all, name='gallarie_all'),
    path('Projects/', Projects, name='Projects'),
    path('events/', events, name='events'),
    path('add_event/', add_event, name='add_event'),
    path('add_event_back/', add_event_back, name='add_event_back'),
    path('events_list/', event_list, name='event_list'),
    
    path('update_event/<int:event_id>/', update_event, name='update_event'),
    path('gallery_list_view/',gallery_list_view, name='gallery_list_view'),
    path('update_gallery_image/<int:image_id>/', update_gallery_image, name='update_gallery_image'),
    path('faq_list/', faq_list, name='faq_list'),
    path('event/<int:event_id>/delete/', delete_event, name='delete_event'),
    
    #new yismu template
    path('gallery_view/', gallery_view, name='gallery_view'),
    path('events_list_new/', events_list_new, name='events_list_new'),
    path('delete_gallery_image/<int:image_id>/', delete_gallery_image, name='delete_gallery_image'),
    path('faq/<int:faq_id>/delete/', delete_faq, name='delete_faq'),


    
    

]

