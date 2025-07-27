from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DeviceProfileViewSet

router = DefaultRouter()
router.register(r'', DeviceProfileViewSet, basename='deviceprofile')

urlpatterns = [
    path('', include(router.urls)),
]
