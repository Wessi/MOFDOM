# admin.py

from django.contrib import admin
from .models import UserProfile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# class UserAdmin(BaseUserAdmin):

#     #form = UserChangeForm
#     # add_form = CustomerCreationForm

#     list_display = ('email','first_name','last_name', 'group', 'is_superuser')
#     list_filter = ('group', )
#     fieldsets = (
#         (None, {'fields': ('email',)}),
#         ('Personal info', {'fields': ('first_name','last_name',)}),
#         ('User Type', {'fields': ('is_active','is_staff','group','status','is_superuser', )}),
#         ('Permissions', {'fields':('user_permissions','group_permissions')}),
#     )
#     # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
#     # overrides get_fieldsets to use this attribute when creating a user.
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'first_name','last_name', 'password1', 'password2', 'group', 'is_superuser', )}
#         ),
#     )
    
#     search_fields = ('email','first_name', 'last_name')
#     ordering = ('email','date_joined')
#     filter_horizontal = ('groups', 'user_permissions')


admin.site.register(UserProfile)
