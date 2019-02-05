from django.urls import path
from .views import DepartmentList, DepartmentCreate, DepartmentUpdate, DepartmentDelete

urlpatterns = [
    path('', DepartmentList.as_view(), name='departments_list'),
    path('new/', DepartmentCreate.as_view(), name='departments_create'),
    path('edit/<int:pk>', DepartmentUpdate.as_view(), name='departments_update'),
    path('delete/<int:pk>', DepartmentDelete.as_view(), name='departments_delete'),
]

