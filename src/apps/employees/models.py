from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from ..departments.models import Department
from ..companies.models import Company

class Employee(models.Model):
    name = models.CharField(max_length=120)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    departments = models.ManyToManyField(Department)
    company = models.ForeignKey(Company, on_delete=models.PROTECT, null=True, blank=True)

    @property
    def total_hours(self):
        total = self.registerhour_set.all().aggregate(Sum('hours'))['hours__sum']
        return total

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('employees_list')
