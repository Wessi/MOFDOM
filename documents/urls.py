# documents/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('document-list/', document_list, name='document_list'),
    path('document-list/', doc_view, name='doc_view'),
    # path('add_doc/', upload_document, name='document_add'),
    # path('document/add/', document_add, name='document_add'),
    path('document-listt/', doc_view, name='doc_view'),
    path('add_document/', add_document, name='add_document'),
    path('document_view/', document_view, name='document_view'),
    #2/24/2024
    path('update_document/<int:document_id>/', update_document, name='update_document'),
    
    # for yismu
    path('list-documents/', list_docs_view, name='list_docs'),
    path('document/<int:document_id>/delete/', delete_document, name='delete_document'),
    path('pdf/<str:pk>/', pdf_view, name='pdf-view'),

]
