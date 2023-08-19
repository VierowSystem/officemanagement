from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from OfficeApp import models
from OfficeApp.models import Login


# admin.site.register(models.User)
admin.site.register(models.Stock)
admin.site.register(models.Account)
admin.site.register(models.Sales)
admin.site.register(models.Expense)
admin.site.register(models.Item)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_manager', 'is_user')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'is_manager', 'is_user')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'is_manager', 'is_user')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_staff', 'is_active', 'is_superuser', 'is_manager', 'is_user')}
        ),
    )

admin.site.register(Login, CustomUserAdmin)

