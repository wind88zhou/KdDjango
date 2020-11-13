from django.contrib import admin
from kdapp.models import Test,BookInfo,HeroInfo


class  ATestAdmin(admin.ModelAdmin):
    list_display = ['id','name']

class BookInfoAdmin(admin.ModelAdmin):
    list_per_page = 5 # 指定每页显示5条数据
    list_display = ['id','btitle','new_title','bpub_data','bread','bcomment','isDelete']
    # 操作栏显示在下面
    actions_on_bottom = False # 显示在下面则设置为True
    actions_on_top = True # 显示在上面则设置为True
    # 新增右侧过滤栏
    list_filter = ['btitle']
    # 新增搜索功能 - 按btitle搜索
    search_fields = ['btitle']
    # 修改编辑页显示顺序
    fields = ['id','btitle','bpub_data','bcomment','bread','isDelete']

# Register your models here.
admin.site.register(Test,ATestAdmin)
admin.site.register(HeroInfo)

admin.site.register(BookInfo,BookInfoAdmin)

