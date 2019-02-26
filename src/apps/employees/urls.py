from django.urls import path
from .views import EmployeesList, EmployeeUpdate, EmployeeDelete, EmployeeCreate, pdf_reportlab, Pdf

urlpatterns = [
    path('', EmployeesList.as_view(), name='employees_list'),
    path('edit/<int:pk>', EmployeeUpdate.as_view(), name='employees_update'),
    path('delete/<int:pk>', EmployeeDelete.as_view(), name='employees_delete'),
    path('new/', EmployeeCreate.as_view(), name='employees_create'),
    path('pdf-reportlab/', pdf_reportlab, name='pdf_reportlab'),
    path('relatorio-html/', Pdf.as_view(), name='relatorio_html'),
]

