from django.db import models

# Create your models here.

class CmDict(models.Model):
    name = models.CharField(primary_key=True, max_length=100) # 字典名，EN
    desc = models.CharField(max_length=100) # 字典描述
    dataType = models.IntegerField()
