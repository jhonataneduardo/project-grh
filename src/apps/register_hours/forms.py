from django.forms import ModelForm
from .models import RegisterHour
from apps.employees.models import Employee


class RegisterHourForm(ModelForm):

    def __init__(self, user, *args, **kwargs):
        super(RegisterHourForm, self).__init__(*args, **kwargs)
        self.fields['employee'].queryset = Employee.objects.filter(
            company=user.employee.company
        )

    class Meta:
        model = RegisterHour
        fields = ['justification', 'hours', 'employee']
