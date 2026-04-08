from django.db import models

class Car(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField(default=2000)
    price = models.IntegerField()

    def __str__(self):
        return self.brand

class Engine(models.Model):
    type = models.CharField(max_length=100)
    weight = models.IntegerField()
    horsepower = models.IntegerField()

    def __str__(self):
        return self.type
# Create your models here.
