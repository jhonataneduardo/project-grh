from django.urls import path
from .views import DocumentCreate
urlpatterns = [
    path('new/<int:employee_id>/', DocumentCreate.as_view(), name='documents_create'),
]

