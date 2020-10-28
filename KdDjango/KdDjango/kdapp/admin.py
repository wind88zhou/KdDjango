from django.contrib import admin
from kdapp.models import Test,BookInfo,HeroInfo


class  ATestAdmin(admin.ModelAdmin):
    list_display = ['id','name']

# Register your models here.
admin.site.register(Test,ATestAdmin,BookInfo,HeroInfo)

