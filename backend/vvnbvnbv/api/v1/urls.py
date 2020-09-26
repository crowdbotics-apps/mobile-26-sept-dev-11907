from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import GghthghjgjViewSet

router = DefaultRouter()
router.register("gghthghjgj", GghthghjgjViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
