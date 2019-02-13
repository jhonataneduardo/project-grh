from django.urls import path
from .views import RegisterHourList

urlpatterns = [
    path('', RegisterHourList.as_view(), name='register_hours_list'),
    # path('edit/<int:pk>', EmployeeUpdate.as_view(), name='employees_update'),
    # path('delete/<int:pk>', EmployeeDelete.as_view(), name='employees_delete'),
    # path('new/', EmployeeCreate.as_view(), name='employees_create'),
]

