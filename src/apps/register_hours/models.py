from django.db import models
from django.urls import reverse

from ..employees.models import Employee


class RegisterHour(models.Model):
    justification = models.CharField(max_length=120)
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)
    hours = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.employee.name

    def get_absolute_url(self):
        return reverse('register_hours_update', args=[self.id])
