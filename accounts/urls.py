from django.urls import path
from .views import *  # Import the faqs_api view

urlpatterns = [
    path('signup/', Signup.as_view(), name="signup"),
    path('login/', Login.as_view(), name="login"),
    path('logout/', Logout.as_view(), name="logout"),
    
    
    path('login-staff/', Login_Staff, name='Login_Staff'),
    path('register/', register, name='register'),
    # path('logout/', Logout_Staff, name='logout'),
    path('Profile_view/',Profile_view, name='Profile_view'),
    path('profile/', profile, name='profile'),

]

