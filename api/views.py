from rest_framework import viewsets

from api.serializers import PostSerializer
from core.models import Post


class PostViewSet(viewsets.ModelViewSet):
    """
    CRUD View Set for DABooks Posts
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # lookup_field = 'title'

    def perform_create(self, serializer: PostSerializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer: PostSerializer):
        serializer.save(author=self.request.user)
