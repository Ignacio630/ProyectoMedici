from django.db import models

# Create your models here.

class Providers(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField()
    