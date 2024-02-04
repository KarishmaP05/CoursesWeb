from django.db import models
from datetime import date

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=300)
    date = models.DateField(default=date.today())
    message = models.TextField()

    def __str__(self):
        return self.name