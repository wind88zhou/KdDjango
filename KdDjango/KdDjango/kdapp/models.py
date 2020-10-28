from django.db import models

# Create your models here.

class Test(models.Model):
    name = models.CharField(max_length=20)

    # 魔法属性，返回数据名称
    def __str__(self):
        return self.name

class BookInfo(models.Model):
    '''图书模型类'''
    btitle = models.CharField(max_length=20)
    bpub_data = models.DateField()
    bread = models.IntegerField(default=0)
    bcomment = models.IntegerField(default=0)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.btitle

class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=False)
    hcomment = models.CharField(max_length=20)
    # 关系属性
    hbook = models.ForeignKey('BookInfo',on_delete=models.CASCADE)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.hname
