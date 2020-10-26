from django.contrib import admin
from kdapp.models import Test


class  ATestAdmin(admin.ModelAdmin):
    list_display = ['id','name']

# Register your models here.
admin.site.register(Test,ATestAdmin)

