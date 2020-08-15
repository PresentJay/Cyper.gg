from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.


@admin.register(models.User)
class Admin(UserAdmin):

    fieldsets = UserAdmin.fieldsets + (
        (
            "Additional",
            {"fields": ("avatar", "gender", "bio", "birthdate", "login_method",),},
        ),
    )

    list_filter = UserAdmin.list_filter

    list_display = (
        "username",
        "email",
        "is_active",
        "email_confirmed",
        "email_secret",
        "login_method",
    )
