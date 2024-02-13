# documents/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('document-list/', document_list, name='document_list'),
    path('document-list/', doc_view, name='doc_view'),
    path('add_doc/', upload_document, name='document_add'),
    path('document_view/', document_view, name='document_view'),
    
    # for yismu
    path('list-documents/', list_docs_view, name='list_docs'),
    path('document/<int:document_id>/delete/', delete_document, name='delete_document'),

]
