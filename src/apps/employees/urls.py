from django.urls import path
from .views import EmployeesList

urlpatterns = [
    path('', EmployeesList.as_view(), name='employees_list'),
]

