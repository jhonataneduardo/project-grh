from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .tasks import send_relatorio
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from apps.base.serializers import UserSerializer, GroupSerializer


def celery(request):
    send_relatorio()
    return HttpResponse('Foi')


@login_required
def base(request):
    data = {}
    data['usuario'] = request.user
    return render(request, 'base/index.html', data)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
