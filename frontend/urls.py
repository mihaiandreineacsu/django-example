# from django.views.generic import TemplateView
from django.urls import path

urlpatterns = [
    path("posts/", PostListView.as_view()),
]
