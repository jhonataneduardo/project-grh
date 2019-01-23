from django.db import models

class Document(models.Model):
    description = models.CharField(max_length=120)

    def __str__(self):
        return self.description
