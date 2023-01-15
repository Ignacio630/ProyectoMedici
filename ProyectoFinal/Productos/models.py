from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.BooleanField()
    category = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return f'{self.name} - {self.price} - {self.stock} - {self.category} - {self.description}'
