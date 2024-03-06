from django.urls import path
from . import views
from .views import delete_supplier
urlpatterns = [
    # Add more URL patterns as needed
    path('supplier/add', views.add_supplier, name='supplier_add'),
    path('locked_supplier_list/', views.view_supplier, name='supplier_list'),
    path('search_supplier/', views.search_supplier, name='search_supplier'),
    path('supplier_admin/view', views.view_supplier_admin, name='supp_admin_view'),
    path('delete_supplier/<int:supplier_id>/', delete_supplier, name='delete_supplier'),
    path('update_supplier/<int:supplier_id>/', views.update_supplier, name='update_supplier'),

]
