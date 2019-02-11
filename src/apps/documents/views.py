from django.views.generic.edit import CreateView
from apps.employees.models import Employee
from .models import Document


class DocumentCreate(CreateView):
    model = Document
    fields = ['description', 'file']

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        form.instance.belongs_to = Employee.objects.filter(id=self.kwargs['employee_id'])[0]
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
