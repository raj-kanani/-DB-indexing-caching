from django.contrib import admin
from .models import *

admin.site.register(Student)


@admin.register(Redis)
class RedisAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'desc']


@admin.register(Movie)
class RedisAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'desc', 'image', 'ticket_price']
