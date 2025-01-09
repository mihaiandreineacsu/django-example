from rest_framework import viewsets

from core.models import Post
from core.serializers import PostSerializer
from .permissions import IsAuthorRequestUser


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorRequestUser]
    # authentication_classes = [authentication.BasicAuthentication]

    def perform_create(self, serializer):
        print("my perform_create")
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        print("my perform_update")
        serializer.save(author=self.request.user)
