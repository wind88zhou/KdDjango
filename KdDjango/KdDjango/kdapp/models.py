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
    
    # class Meta:
    #     db_table = "bookinfo"  # 指定模型类对应的表名

    def new_title(self):
        return self.btitle
    # 支持在admin页面点击 new_title进行排序
    new_title.admin_order_field = 'btitle'
    # 新列显示汉字
    new_title.short_description = '新标题'


class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=False)
    hcomment = models.CharField(max_length=20)
    # 关系属性
    hbook = models.ForeignKey('BookInfo',on_delete=models.CASCADE)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.hname


# 上传图片的类
class PicTest(models.Model):
    goods_pic = models.ImageField(upload_to = 'kdapp')