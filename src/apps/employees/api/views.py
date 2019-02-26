from apps.employees.models import Employee
from rest_framework import viewsets
from apps.employees.api.serializers import EmployeeSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class EmployeeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
