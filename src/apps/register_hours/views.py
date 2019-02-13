from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import UpdateView
from .models import RegisterHour


class RegisterHourList(ListView):
    model = RegisterHour
    fields = ['justification', 'hours', 'employee']

    def get_queryset(self):
        company_current = self.request.user.employee.company
        return RegisterHour.objects.filter(employee__company=company_current)


class RegisterUpdate(UpdateView):
    model = RegisterHour
    fields = ['justification', 'hours', 'employee']
