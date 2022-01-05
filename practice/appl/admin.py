from django.contrib import admin

from .models import function
class classadmin(admin.ModelAdmin):
    list_display = ['id','name','phone','address']
admin .site.register(function,classadmin)

# Register your models here.
