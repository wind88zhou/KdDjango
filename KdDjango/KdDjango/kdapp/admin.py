from django.contrib import admin
from kdapp.models import Test,BookInfo,HeroInfo


class  ATestAdmin(admin.ModelAdmin):
    list_display = ['id','name']

# Register your models here.
admin.site.register(Test,ATestAdmin)
admin.site.register([BookInfo,HeroInfo])

admin.site.register(BookInfo,BookInfoAdmin)

class BookInfoAdmin(admin.ModelAdmin):
    list_per_page = 5 # 指定每页显示5条数据