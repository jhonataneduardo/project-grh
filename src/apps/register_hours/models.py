from django.db import models

class RegisterHour(models.Model):
    justification = models.CharField(max_length=120)
