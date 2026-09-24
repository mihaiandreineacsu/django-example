"""
URL mappings for the core app.
"""

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()
router.register("posts", views.PostViewSet)

app_name = "api"

urlpatterns = [
    path("", include(router.urls)),
]
