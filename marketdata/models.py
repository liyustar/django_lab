from django.db import models

# Create your models here.

class SecuInfo(models.Model):
    symbol = models.CharField(max_length=50)
    market = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
