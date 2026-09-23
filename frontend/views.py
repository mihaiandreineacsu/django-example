from django.views.generic import ListView

from core.models import Post


# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = "posts.html"
