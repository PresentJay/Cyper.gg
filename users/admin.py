from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.


# @admin.register(models.User)
@admin.register(models.User)
class Admin(UserAdmin):

    fieldsets = UserAdmin.fieldsets + (
        ("Additional", {"fields": ("avatar", "gender", "bio", "birthdate",),}),
    )
