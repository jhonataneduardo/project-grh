from apps.register_hours.models import RegisterHour
from rest_framework import viewsets
from apps.register_hours.api.serializers import RegisterHourSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class RegisterHourViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = RegisterHour.objects.all()
    serializer_class = RegisterHourSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
