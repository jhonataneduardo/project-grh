from apps.employees.models import Employee
from apps.register_hours.api.serializers import RegisterHourSerializer
from rest_framework import serializers


class EmployeeSerializer(serializers.ModelSerializer):
    registerhour_set = RegisterHourSerializer(many=True)

    class Meta:
        model = Employee
        fields = ('name', 'user', 'departments', 'company', 'registerhour_set')
