from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
class UserProfile(AbstractUser):
    USER_ROLES = (
        ('admin', 'Admin'),
        ('teamleader', 'Team Leader'),
        ('author', 'Author'),
        ('editor', 'Editor'),
        ('visitor', 'Visitor'),
    )
    role = models.CharField(max_length=20, choices=USER_ROLES, default='visitor')
    profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    phonenumber = models.CharField(max_length=15, null=True, blank=True)
# Add related_name attributes to avoid clashes
    groups = models.ManyToManyField(Group, blank=True, related_name='user_profiles')
    user_permissions = models.ManyToManyField(
        Permission, blank=True, related_name='user_profiles_permissions'
    )
