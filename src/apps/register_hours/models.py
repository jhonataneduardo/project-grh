from django.db import models
from ..employees.models import Employee
class RegisterHour(models.Model):
    justification = models.CharField(max_length=120)
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)
