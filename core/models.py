from django.db import models
from django.contrib.auth.models import User
from django.db.models.functions import Lower
from colorfield.fields import ColorField


def get_or_create_uncategorized():
    """
    Get the 'Uncategorized' category, or create it if it doesn't exist.
    """
    category, created = Category.objects.get_or_create(
        name="Uncategorized", defaults={"color": "#000000"}  # Set a default color if creating a new category
    )
    return category


class Category(models.Model):
    """
    The Core Model for Categories
    """

    COLOR_PALETTE = [
        (
            "#FFFFFF",
            "white",
        ),
        (
            "#000000",
            "black",
        ),
    ]

    name = models.CharField(max_length=80, null=False, blank=False, unique=True, help_text="The name of Post category.")
    color = ColorField(choices=COLOR_PALETTE)

    class Meta:
        verbose_name_plural = "Categories"
        constraints = [
            models.UniqueConstraint(
                Lower("name"),
                name="unique_lower_name",
                violation_error_message="This Name already exists (Capital- and Lowercase is ignored).",
            )
        ]

    def delete(self, *args, **kwargs):
        """
        Protect the uncategorized Category because is used as Fallback to be set on Posts ForeignKey
            when deleting other Categories.
        """
        if self.name.lower() == "uncategorized":
            raise ValueError("The 'Uncategorized' category cannot be deleted.")
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.name


# Create your models here.
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
    category = models.ForeignKey(
        to=Category,
        on_delete=models.SET(get_or_create_uncategorized),
        null=False,
        blank=False,
        help_text="Category that matches the Post content.",
    )


# TODO Create Categories for Posts -> ManyToMany
# Fields Constrains
# Sub Categories -> Example: Main Category "News" then Sb Categories like : "Sport", "Politic" etc...
# Fields:
#   - Name: unique constrain Ex. Sport == sport :checked:
#   - Color: Django Color Package?
#   - Description
#   - Parent Category: Model Category (How to resolve Infinite Loop?)
#
# Test Feature 1 Bug fix
# Test Feature 2
