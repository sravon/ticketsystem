from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Tickets(models.Model):
    number = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    priority = models.CharField(max_length=200)

    def __str__(self):
        return self.description
