from django.contrib import admin
from .models import *

admin.site.register(Student)


@admin.register(Redis)
class RedisAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'desc']

