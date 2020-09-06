from django.db import models

# Create your models here.

class Portfolio(models.Model):
    username = models.CharField(max_length=6, primary_key=True)
    etfs = models.CharField()
    futures = models.CharField()
    bonds = models.CharField()
    equities = models.CharField()
    options = models.CharField()