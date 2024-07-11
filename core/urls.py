"""
URL mappings for the core app.
"""
from django.urls import (
    path,
    include,
)
from rest_framework.routers import DefaultRouter
from core import views

router = DefaultRouter()
router.register('tasks', views.PostViewSet)

app_name = 'core'

urlpatterns = [
    path('', include(router.urls)),
]