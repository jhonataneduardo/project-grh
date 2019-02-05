from django.contrib.auth.models import User
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Employee


class EmployeesList(ListView):
    model = Employee

    def get_queryset(self):
        company_current = self.request.user.employee.company
        return Employee.objects.filter(company=company_current)


class EmployeeUpdate(UpdateView):
    model = Employee
    fields = ['name', 'departments']


class EmployeeDelete(DeleteView):
    model = Employee
    success_url = reverse_lazy('employees_list')


class EmployeeCreate(CreateView):
    model = Employee
    fields = ['name', 'departments']

    def form_valid(self, form):
        obj = form.save(commit=False)
        username = obj.name.split(" ")
        obj.company = self.request.user.employee.company
        obj.user = User.objects.create(username=username[0])
        return super(EmployeeCreate, self).form_valid(form)
