from typing import Any

from colorfield.fields import ColorField
from django.contrib.auth.models import User
from django.db import models
from django.db.models.functions import Lower
from typing_extensions import override


def post_directory_path(instance: "Post", filename: str) -> str:
    # file will be uploaded to MEDIA_ROOT/post_<id>/<filename>
    return "post_{0}/{1}".format(instance.id, filename)


def get_or_create_uncategorized():
    """
    Get the 'Uncategorised' category, or create it if it doesn't exist.
    """
    category, _ = Category.objects.get_or_create(
        name="Uncategorised", defaults={"color": "#000000"}  # Set a default color if creating a new category
    )
    return category


class Category(models.Model):
    """
    The Core Model for Categories
    """

    name = models.CharField(
        max_length=80, null=False, blank=False, unique=True, help_text="The unique name of Post category."
    )
    color = ColorField(null=False, blank=False, unique=True, help_text="The unique color of category.")

    class Meta:
        verbose_name_plural = "Categories"
        constraints = [
            models.UniqueConstraint(
                Lower("name"),
                name="unique_lower_name",
                violation_error_message="This Name already exists (Capital- and Lowercase is ignored).",
            ),
            models.UniqueConstraint(
                Lower("color"),
                name="unique_lower_color",
                violation_error_message="This color already exists (Capital- and Lowercase is ignored).",
            ),
            models.CheckConstraint(
                condition=(~models.Q(name="")), name="name_populated", violation_error_message="Name can not be empty!"
            ),
            models.CheckConstraint(
                condition=(~models.Q(color="")),
                name="color_populated",
                violation_error_message="Color can not be empty!",
            ),
            models.CheckConstraint(
                condition=~models.Q(parent_category=models.F("id")),
                name="prevent_self_reference",
                violation_error_message="Category cannot reference itself!",
            ),
        ]

    parent_category = models.ForeignKey(
        "self", on_delete=models.CASCADE, related_name="subordinates", null=True, blank=True
    )

    @override
    def delete(self, *args: bool, **kwargs: dict[str, Any]) -> tuple[int, dict[str, int]]:
        """
        Protect the uncategorized Category because is used as Fallback to be set on Posts ForeignKey
            when deleting other Categories.
        """
        if self.name.lower() == "uncategorized":
            raise ValueError("The 'Uncategorised' category cannot be deleted.")
        return super().delete(*args, **kwargs)

    def __str__(self):
        return self.name


class Post(models.Model):
    """
    The Core Model for DABooks Posts
    """

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, null=False, blank=False, help_text="The author that created the Post."
    )
    title = models.CharField(
        max_length=100, null=False, blank=False, help_text="Post title given by author when creating it."
    )
    description = models.TextField(
        max_length=1000, null=False, blank=True, default="", help_text="A description what this post is about."
    )

    image = models.ImageField(
        upload_to=post_directory_path,  # MEDIA_ROOT / posts
        null=True,
        blank=True,
        help_text="An image that represents the post.",
    )

    categories = models.ManyToManyField(to=Category, through="core.PostCategory", related_name="posts")


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_created = models.DateField(auto_created=True)
