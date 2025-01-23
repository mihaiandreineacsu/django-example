from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    """
    The Core Models for DABooks Posts
    """

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, null=False, blank=False, help_text="The author that created the Post."
    )
    title = models.CharField(
        max_length=250, null=False, blank=False, help_text="Post title given by author when creating it."
    )
    description = models.CharField(max_length=1000, null=False, blank=True, default="")


# TODO Create Categories for Posts -> ManyToMany
# Fields Constrains
# Sub Categories -> Example: Main Category "News" then Sb Categories like : "Sport", "Politic" etc...
# Fields:
#   - Name:
#   - Color: Django Color Package?
#   - Description
#   - Parent Category: Model Category (How to resolve Infinite Loop?)
#

# Test Feature 1
# Test Feature 2
