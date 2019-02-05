from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Department


class DepartmentList(ListView):
    model = Department

    def get_queryset(self):
        company_current = self.request.user.employee.company
        return Department.objects.filter(company=company_current)


class DepartmentCreate(CreateView):
    model = Department
    fields = ['name']

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.company = self.request.user.employee.company
        obj.save()
        return super(DepartmentCreate, self).form_valid(form)


class DepartmentUpdate(UpdateView):
    model = Department
    fields = ['name']


class DepartmentDelete(DeleteView):
    model = Department
    success_url = reverse_lazy('departments_list')
