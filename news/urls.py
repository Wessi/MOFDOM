from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='news_home'),
    # Add more URL patterns as needed
    path('news/<int:news_id>/', views.news_detail, name='news_detail'),  # Front News Details Page
    path('panel/news/list/', views.news_list, name='news_list'),  # Admin Panel News List
    path('index/', views.index_news, name='index'),
    path('add_news/', views.add_news_admin, name='add_news'),

    path('newsarticle/', views.news_article_list, name='news_article_list'),
    path('add_news_article/', views.add_news_article, name='add_news_article'),
    path('news_add_back/', views.news_add_back, name='news_add_back'),
    
    path('news_view/', views.news_list_visitor, name='news_list_visitor'),
    path('news-article/<int:article_id>/delete/', views.delete_news_article, name='delete_news_article'),
    
]
