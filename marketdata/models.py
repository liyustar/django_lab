from django.db import models

# Create your models here.

class SecuInfo(models.Model):
    symbol = models.CharField(max_length=50)
    market = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    creator = models.ForeignKey('auth.User', related_name='secu_infos', on_delete=models.CASCADE)

    def __str__(self):
        return "%s.%s" % (self.symbol, self.market)
