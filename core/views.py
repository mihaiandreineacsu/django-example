from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import authentication

from core.models import Post
from core.serializers import PostSerializer
from rest_framework.response import Response
from rest_framework import status


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.SessionAuthentication]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.author != self.request.user.id:
            return Response(status=status.HTTP_403_FORBIDDEN)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_create(self, serializer):
        print("my perform_create")
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        print("my perform_update")
        serializer.save(author=self.request.user)