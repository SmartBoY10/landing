from django.contrib import admin
from .models import *


@admin.register(WorkingTime)
class WorkingTimeAdmin(admin.ModelAdmin):
    list_display = ("id", "date", "norm_hour", "hour")
    list_display_links = ("id", "date")

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name")
    list_display_links = ("id", "full_name")