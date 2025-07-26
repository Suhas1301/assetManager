from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AssetProfileViewSet

router = DefaultRouter()
router.register(r'assetprofile', AssetProfileViewSet, basename='assetprofile')

urlpatterns = [
    path('', include(router.urls)),
]
