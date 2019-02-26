from django.contrib.auth.models import User
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, View
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Employee

# Used for lib reportab
import io
from reportlab.pdfgen import canvas

# used for lib xhtml2pdf
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa

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


def pdf_reportlab(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="pdfteste.pdf"'

    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)

    p.drawString(10, 810, "Hello, Word!")

    palavras = ['palavra1', 'palavra2', 'palavra2']

    y = 790
    for palavra in palavras:
        p.drawString(10, y, palavra)
        y -= 40

    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response


class Render:

    @staticmethod
    def render(path: str, params: dict, filename: str):
        template = get_template(path)
        html = template.render(params)
        response = io.BytesIO()
        pdf = pisa.pisaDocument(io.BytesIO(html.encode("UTF-8")), response)
        if not pdf.err:
            response = HttpResponse(response.getvalue(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename=%s.pdf' % filename
            return response
        else:
            return HttpResponse("Error Redering PDF", status=500)


class Pdf(View):

    def get(self, request):
        params = {
            'today': 'Variavel teste today',
            'sales': 'Variavel teste sales',
            'request': request,
        }
        return Render.render('employees/relatorio.html', params, 'testenovo')
