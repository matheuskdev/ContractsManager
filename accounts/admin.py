from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdminModel(admin.ModelAdmin):
    list_display = [
        "email",
        "username",
        "first_name",
        "last_name",
    ]
    readonly_fields = [
        "last_login",
        "date_joined",
    ]
