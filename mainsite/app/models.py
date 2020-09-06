from django.db import models

# Create your models here.

class Portfolio(models.Model):
    username = models.CharField(max_length=100, primary_key=True)
    etfs = models.CharField(max_length=10)
    futures = models.CharField(max_length=10)
    bonds = models.CharField(max_length=10)
    equities = models.CharField(max_length=10)
    options = models.CharField(max_length=10)