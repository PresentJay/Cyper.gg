from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.User)
class Admin(admin.ModelAdmin):
    """Admin View for """

    list_display = ("",)
    list_filter = ("",)
    inlines = []
    raw_id_fields = ("",)
    readonly_fields = ("",)
    search_fields = ("",)
    date_hierarchy = ""
    ordering = ("",)
