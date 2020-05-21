from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MyUsermodel

class user_admin(UserAdmin):
    orderimg = ['id']
    list_display = ['email',]
    fieldsets = (
        (None, {'fields': ('email', 'password', 'username', 'date_of_birth',)}),
        ('permissions', {'fields': ('is_active', 'is_admin', 'is_staff',)}),
    )

admin.site.register(MyUsermodel, user_admin)

