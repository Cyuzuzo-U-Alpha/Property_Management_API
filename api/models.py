from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Owner(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=50)

class Property(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    address = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

