from django.shortcuts import render
from rest_framework import viewsets
from .models import DeviceProfile
from .serializers import DeviceProfileSerializer

class DeviceProfileViewSet(viewsets.ModelViewSet):
    queryset = DeviceProfile.objects.all().order_by('-id')
    serializer_class = DeviceProfileSerializer
# Create your views here.