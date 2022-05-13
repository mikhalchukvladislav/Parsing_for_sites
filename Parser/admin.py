from django.contrib import admin
from .models import News, Url
# Register your models here.

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    pass

@admin.register(Url)
class UrlAdmin(admin.ModelAdmin):
    list_display = ['link']