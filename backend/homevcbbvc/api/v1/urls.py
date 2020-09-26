from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import HgjhgkjgkjViewSet

router = DefaultRouter()
router.register("hgjhgkjgkj", HgjhgkjgkjViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
