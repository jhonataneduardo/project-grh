from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import RegisterHour
from .forms import RegisterHourForm


class RegisterHourList(ListView):
    model = RegisterHour
    fields = ['justification', 'hours', 'employee']

    def get_queryset(self):
        company_current = self.request.user.employee.company
        return RegisterHour.objects.filter(employee__company=company_current)


class RegisterHourUpdate(UpdateView):
    model = RegisterHour
    form_class = RegisterHourForm

    def get_form_kwargs(self):
        kwargs = super(RegisterHourUpdate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class RegisterHourDelete(DeleteView):
    model = RegisterHour
    success_url = reverse_lazy('register_hours_list')


class RegisterHourCreate(CreateView):
    model = RegisterHour
    form_class = RegisterHourForm

    def get_form_kwargs(self):
        kwargs = super(RegisterHourCreate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs
