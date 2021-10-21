from django.db import models
from django.utils import timezone


# Create your models here.
class Api_Info(models.Model):
    api_name = models.CharField(max_length=254)
    api_url = models.CharField(max_length=254)
    api_method = models.CharField(max_length=254)
    api_params = models.CharField(max_length=254)
    api_dsc = models.CharField(max_length=254)
    api_creat_time = models.DateTimeField(default=timezone.now)
    api_update_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.api_name

    class Meta:
        db_table = "apiinfo"  # 指定模型类对应的表名
