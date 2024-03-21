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
    company_name = models.CharField(max_length=255,help_text="Make sure to submit a max of 255 characters.")
    legal_form = models.CharField(max_length=100,help_text="Make sure to submit a max of 100 characters.")
    nationality = models.CharField(max_length=100,help_text="Make sure to submit a max of 100 characters.")
    area_of_business = models.CharField(max_length=255,help_text="Make sure to submit a max of 255 characters.")
    sector = models.CharField(max_length=100, choices=SECTOR_CHOICES,help_text="Make sure to submit a max of 100 characters.")
    
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
    
    