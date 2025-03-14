from rest_framework import serializers
from core.models import Post


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        exclude = ("id",)
        read_only_fields = [
            "author",
        ]
