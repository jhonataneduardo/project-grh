from django.urls import path
from .views import RegisterHourList, RegisterHourUpdate, RegisterHourDelete, RegisterHourCreate

urlpatterns = [
    path('', RegisterHourList.as_view(), name='register_hours_list'),
    path('edit/<int:pk>', RegisterHourUpdate.as_view(), name='register_hours_update'),
    path('delete/<int:pk>', RegisterHourDelete.as_view(), name='register_hours_delete'),
    path('new/', RegisterHourCreate.as_view(), name='register_hours_create'),
]

