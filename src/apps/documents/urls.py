from django.urls import path
from .views import DocumentCreate
urlpatterns = [
    path('new', DocumentCreate.as_view(), name='documents_create'),
]

