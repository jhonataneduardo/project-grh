from apps.register_hours.models import RegisterHour
from rest_framework import viewsets
from apps.register_hours.api.serializers import RegisterHourSerializer

class RegisterHourViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = RegisterHour.objects.all()
    serializer_class = RegisterHourSerializer
