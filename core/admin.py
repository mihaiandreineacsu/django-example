from django.contrib import admin
from core.models import Category, Post


# Register your models here.


@admin.register(Post, Category)
class CoreAdmin(admin.ModelAdmin):
    pass
