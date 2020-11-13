from django.contrib import admin
from kdapp.models import Test,BookInfo,HeroInfo


class  ATestAdmin(admin.ModelAdmin):
    list_display = ['id','name']

class BookInfoAdmin(admin.ModelAdmin):
    list_per_page = 5 # 指定每页显示5条数据
    list_display = ['id','btitle','new_title','bpub_data','bread','bcomment','isDelete']
    # 操作栏显示在下面
    actions_on_bottom = True
    actions_on_top = False

# Register your models here.
admin.site.register(Test,ATestAdmin)
admin.site.register(HeroInfo)

admin.site.register(BookInfo,BookInfoAdmin)

