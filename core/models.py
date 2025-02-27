from django.db import models
from django.contrib.auth.models import User
from django.db.models.functions import Lower


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


class Category(models.Model):
    """
    The Core Model for Categories
    """

    name = models.CharField(max_length=80, null=False, blank=False, unique=True, help_text="The name of Post category.")

    class Meta:
        verbose_name_plural = "Categories"
        constraints = [
            models.UniqueConstraint(
                Lower("name"),
                name="unique_lower_name",
                violation_error_message="This Name already exists (Capital- and Lowercase is ignored).",
            )
        ]


# TODO Create Categories for Posts -> ManyToMany
# Fields Constrains
# Sub Categories -> Example: Main Category "News" then Sb Categories like : "Sport", "Politic" etc...
# Fields:
#   - Name: unique constrain Ex. Sport == sport
#   - Color: Django Color Package?
#   - Description
#   - Parent Category: Model Category (How to resolve Infinite Loop?)
#
# Test Feature 1 Bug fix
# Test Feature 2
