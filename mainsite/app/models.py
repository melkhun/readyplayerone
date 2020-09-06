from django.db import models

# Create your models here.

class Portfolio(models.Model):
    username = models.CharField(max_length=100)
    category = models.CharField(max_length=30)
    symbol = models.CharField(max_length=30)