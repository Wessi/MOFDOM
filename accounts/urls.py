from django.urls import path
from .views import *  # Import the faqs_api view
from . import password_manager

from django.contrib.auth import views as pw_views

urlpatterns = [
    path('signup/', Signup.as_view(), name="signup"),
    path('login/', Login.as_view(), name="login"),
    path('logout/', Logout.as_view(), name="logout"),
    
    
    path('login-staff/', Login_Staff, name='Login_Staff'),
    path('register/', register, name='register'),
    # path('logout/', Logout_Staff, name='logout'),
    path('Profile_view/',Profile_view, name='Profile_view'),
    path('profile/<int:id>', Profile.as_view(), name='profile'),
    path('change_pw/<int:id>', ChangePassword.as_view(), name='change_pw'),

    # reset pw urls 

    path('reset_password/', pw_views.PasswordResetView.as_view(template_name='password_reset.html'), name='reset_password'),
    path('reset_password_sent/', pw_views.PasswordResetDoneView.as_view(template_name='pw_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', password_manager.PasswordResetConfirmView.as_view(template_name='pw_reset_form.html'), name='password_reset_confirm'),
    path('reset_password_complete/', pw_views.PasswordResetCompleteView.as_view(template_name='pw_reset_complete.html'), name='password_reset_complete'),
]

