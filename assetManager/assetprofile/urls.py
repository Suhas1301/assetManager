from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AssetProfileViewSet

router = DefaultRouter()
router.register(r'assetprofiles', AssetProfileViewSet, basename='assetprofile')

urlpatterns = [
    path('', include(router.urls)),
]
