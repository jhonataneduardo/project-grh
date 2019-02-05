from django.urls import path
from .views import EmployeesList, EmployeeUpdate, EmployeeDelete, EmployeeCreate

urlpatterns = [
    path('', EmployeesList.as_view(), name='employees_list'),
    path('edit/<int:pk>', EmployeeUpdate.as_view(), name='employees_update'),
    path('delete/<int:pk>', EmployeeDelete.as_view(), name='employees_delete'),
    path('new/', EmployeeCreate.as_view(), name='employees_create'),
]

