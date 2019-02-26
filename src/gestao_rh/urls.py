from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from apps.base.views import UserViewSet, GroupViewSet
from apps.employees.api.views import EmployeeViewSet
from apps.register_hours.api.views import RegisterHourViewSet


# Rest Framework
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'api/employees', EmployeeViewSet)
router.register(r'api/hours-extras', RegisterHourViewSet)

urlpatterns = [
    path('', include('apps.base.urls')),
    path('employees/', include('apps.employees.urls')),
    path('departaments/', include('apps.departments.urls')),
    path('documents/', include('apps.documents.urls')),
    path('hours-extras/', include('apps.register_hours.urls')),
    path('company/', include('apps.companies.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),

    # Rest Framework
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
