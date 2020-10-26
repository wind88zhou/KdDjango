from django.db import models

# Create your models here.

class Test(models.Model):
    name = models.CharField(max_length=20)

    # 魔法属性，返回数据名称
    def __str__(self):
        return self.name
