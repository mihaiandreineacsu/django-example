from django.contrib import admin
from core.models import Post


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    fields = "__all__"
    list_display = ["author", "title"]


admin.site.register(Post)
