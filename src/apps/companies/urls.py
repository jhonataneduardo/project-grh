from django.urls import path
from .views import CompanyCreate, CompanyUpdate

urlpatterns = [
    path('new/', CompanyCreate.as_view(), name='company_create'),
    path('edit/<int:pk>/', CompanyUpdate.as_view(), name='company_update'),
]

