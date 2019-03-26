from django.urls import path
from .views import base, celery

urlpatterns = [
    path('', base, name='home'),
    path('celery/', celery, name='celery')
]

