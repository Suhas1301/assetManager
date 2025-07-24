from rest_framework import serializers
from .models import AssetProfile
from django.utils import timezone

class AssetProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetProfile
        fields = ['id', 'name', 'created_date', 'created_time', 'entity_type']
        read_only_fields = ['id', 'created_date', 'created_time', 'entity_type']

    def create(self, validated_data):
        # Auto-fill created_date, created_time, and entity_type
        validated_data['created_date'] = timezone.now().date()
        validated_data['created_time'] = timezone.now().time()
        validated_data['entity_type'] = 'ASSET_PROFILE'
        return super().create(validated_data)
