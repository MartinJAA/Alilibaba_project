from django.db import models
import datetime
#makemigrations
#migrate
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=60)
    image = models.URLField()
    sku = models.IntegerField(default=1)
    valoration = models.IntegerField(default=5)
    price = models.FloatField(default=0.00)

    def __str__(self) -> str:
        return f'{self.sku} - {self.name}'

class Search(models.Model):
    search= models.CharField(max_length=30)
    dateInput=models.DateTimeField(default= datetime.datetime.now())

    def __str__(self) -> str:
        return f'{self.search}'