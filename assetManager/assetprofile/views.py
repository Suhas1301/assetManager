from django.shortcuts import render
from rest_framework import viewsets
from .models import AssetProfile
from .serializers import AssetProfileSerializer

class AssetProfileViewSet(viewsets.ModelViewSet):
    queryset = AssetProfile.objects.all().order_by('-id')
    serializer_class = AssetProfileSerializer
# Create your views here.
