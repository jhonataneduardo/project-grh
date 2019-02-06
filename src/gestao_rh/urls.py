from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('apps.base.urls')),
    path('employees/', include('apps.employees.urls')),
    path('departaments/', include('apps.departments.urls')),
    path('documents/', include('apps.documents.urls')),
    path('company/', include('apps.companies.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
