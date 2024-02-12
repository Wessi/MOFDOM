from django.urls import path
from .views import *  # Import the faqs_api view

urlpatterns = [
    path('login-staff/', Login_Staff, name='Login_Staff'),
    path('register/', register, name='register'),
    path('logout/', Logout_Staff, name='logout'),
    path('Profile_view/',Profile_view, name='Profile_view'),
    path('profile/', profile, name='profile'),

]

