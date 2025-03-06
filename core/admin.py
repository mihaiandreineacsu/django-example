from django.contrib import admin
from core.models import Category, Post
from django.utils.safestring import mark_safe


class PostInline(admin.StackedInline):  # Or admin.TabularInline for a table layout
    model = Post
    extra = 1  # Number of empty forms to display


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "color_display")
    search_fields = ("name",)
    inlines = [PostInline]  # Show Post entries inside the Category admin page

    def color_display(self, obj: Category):
        return mark_safe(
            f'<div style="width: 30px; height: 30px; background-color: {obj.color}; border: 1px solid #ccc;"></div>'
        )

    color_display.short_description = "Color Preview"  # Label for the admin panel


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("author", "title", "category")
    search_fields = (
        "title",
        "description",
    )
    list_filter = ("author", "category")
