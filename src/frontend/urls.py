# from django.views.generic import TemplateView
from django.urls import path

from frontend.views import PostListView

urlpatterns = [
    path("posts/", PostListView.as_view()),
]
