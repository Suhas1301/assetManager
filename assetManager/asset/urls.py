from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AssetViewSet

router = DefaultRouter()
router.register(r'asset', AssetViewSet, basename='asset')

urlpatterns = [
    path('', include(router.urls)),
]
