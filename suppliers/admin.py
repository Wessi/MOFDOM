from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Supplier

admin.site.register(Supplier)
#admin.site.register(BlockedSuppliers)
#admin.site.register(BlockedSuppliersHistory)