from django.db import models
from ..employees.models import Employee

class Document(models.Model):
    description = models.CharField(max_length=120)
    belongs_to = models.ForeignKey(Employee, on_delete=models.PROTECT)
    file = models.FileField(upload_to='files')

    def __str__(self):
        return self.description
