from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

class Supplier(models.Model):
    SECTOR_CHOICES = [
        ('Private', _('Private')),
        ('Corporate', _('Corporate')),
        ('Retail', _('Retail')),
        ('Merchant', _('Merchant')),
    ]
    tin = models.CharField(max_length=20)
    company_name = models.CharField(max_length=100)
    legal_form = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    area_of_business = models.CharField(max_length=100)
    sector = models.CharField(max_length=100, choices=SECTOR_CHOICES)
    
    @property
    def get_name(self):
        return self.company_name

    @property
    def get_id(self):
        return self.user.id

    def __str__(self):
        return self.company_name
    def get_list_fields():
        return ['company_name', 'tin', 'nationality', 'area_of_business']
    
    list_fields = get_list_fields()
    
    
class BlockedSupplier(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    reason = models.TextField()
    blocked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.supplier.company_name} - Blocked at {self.blocked_at}"