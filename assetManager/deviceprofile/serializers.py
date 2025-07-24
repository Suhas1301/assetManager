from rest_framework import serializers
from .models import DeviceProfile
from django.utils import timezone

class DeviceProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceProfile
        fields = ['id', 'name', 'created_date', 'created_time', 'entity_type']
        read_only_fields = ['id', 'created_date', 'created_time', 'entity_type']

    def create(self, validated_data):
        # Auto-fill created_date, created_time, and entity_type
        validated_data['created_date'] = timezone.now().date()
        validated_data['created_time'] = timezone.now().time()
        validated_data['entity_type'] = 'DEVICE_PROFILE'
        return super().create(validated_data)
