from rest_framework import serializers
from core.models import Post

class PostSerializer(serializers.ModelSerializer):

    # TODO exclude id and author from payload

    class Meta:
        model = Post
        fields = '__all__'