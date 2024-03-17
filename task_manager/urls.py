from django.urls import path
from .views import *  
urlpatterns = [
     #path('task_view/', task_list_view, name='custom_admin'),
     path('task_view/<str:type>', task_list_view, name='task_list_view'),
     path('create_task/', create_task, name='create_task'),
     #path('task_details/', task_details, name='create_task'),
     path('task_details/<int:task_id>/', TaskDetailsView.as_view(), name='task_details'),
     path('delete_task/<int:task_id>/', delete_task, name='delete_task'),
     path('add_comment/<int:task_id>/', add_comment, name='add_comment'),
     path('reply_comment/<int:comment_id>/', reply_comment, name='reply_comment'),

]
