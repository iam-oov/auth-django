from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin


@admin.register(get_user_model())
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Detail', {'fields': ('height',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Detail', {'fields': ('height',)}),
    )
