from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('apps.base.urls')),
    path('employees/', include('apps.employees.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]
