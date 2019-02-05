from django.http import HttpResponse
from django.views.generic import ListView
from .models import Employee


class EmployeesList(ListView):
    model = Employee

    def get_queryset(self):
        company_current = self.request.user.employee.company
        return Employee.objects.filter(company=company_current)
