from django.contrib import admin
from .models import *


@admin.register(WorkingTime)
class WorkingTimeAdmin(admin.ModelAdmin):
    list_display = ("id", "date", "norm_hour", "hour")
    list_display_links = ("id", "date")

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name", "_get_days", "_get_total")
    list_display_links = ("id", "full_name")

    def _get_days(self, obj):
        hours = Employee.objects.get(id=obj.id).an_hour_a_day.all()
        day = {}
        for hour in hours:
            day[f"{hour.date}"] = f"{hour.hour}/{hour.norm_hour}"
        return day

    def _get_total(self, obj):
        hours = Employee.objects.get(id=obj.id).an_hour_a_day.all()
        hours_worked = 0
        norm_hour = 0
        for day in hours:
            hours_worked += day.hour
            norm_hour += day.norm_hour

        total = {hours_worked: norm_hour}
        return total


    _get_days.short_description = "Days"
    _get_total.short_description = "Total"