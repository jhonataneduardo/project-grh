from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView
from .models import RegisterHour


class RegisterHourList(ListView):
    model = RegisterHour
    fields = ['justification', 'hours', 'employee']

    def get_queryset(self):
        company_current = self.request.user.employee.company
        return RegisterHour.objects.filter(employee__company=company_current)


class RegisterHourUpdate(UpdateView):
    model = RegisterHour
    fields = ['justification', 'hours', 'employee']


class RegisterHourDelete(DeleteView):
    model = RegisterHour
    success_url = reverse_lazy('register_hours_list')
