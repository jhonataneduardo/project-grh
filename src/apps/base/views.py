from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.employees.models import Employee


@login_required
def base(request):
    data = {}
    data['usuario'] = request.user
    return render(request, 'base/index.html', data)
