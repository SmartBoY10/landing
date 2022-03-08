from datetime import date
from django.db import models


class WorkingTime(models.Model):
    date = models.DateField(verbose_name="День", auto_now_add=True)
    norm_hour = models.FloatField(verbose_name="Часы по нормативу", default=8)
    hour = models.FloatField(verbose_name="Часы отработана")


class Employee(models.Model):
    full_name = models.CharField(verbose_name="Работник", max_length=100)
    an_hour_a_day = models.ManyToManyField(WorkingTime, verbose_name="Час в день")

    def __str__(self):
        return self.full_name
