from django.urls import path
from .views import *  # Import the faqs_api view

urlpatterns = [
    path('add_job/', add_vacancy, name='add_job'),
    path('post_job_view/', post_job_view, name='post_job_view'),
    path('jobs/', job_list, name='job_list'),# Updated URL pattern
    path('jobs_view/', jobs_view, name='jobs_view_details'),
    path('vacancy_board/', vacancy_board, name='vacancy_board'),
    path('jobs_detail/<int:job_id>/', jobs_detail, name='jobs_detail'),
    path('job_list_admin/', job_list_admin, name='job_list_admin'),
    path('job_list/', job_list_ytemplate, name='job_list_ytemplate'),
    path('job/<int:job_id>/delete/', delete_job, name='delete_job'),
]

