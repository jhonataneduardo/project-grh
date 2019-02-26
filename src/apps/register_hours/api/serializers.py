from apps.register_hours.models import RegisterHour
from rest_framework import serializers


class RegisterHourSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterHour
        fields = ('justification', 'employee', 'hours', 'is_used')
