from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    title = models.CharField(max_length=250, null=False, blank=False)
    description = models.CharField(max_length=1000, null=False, blank=True, default="")
