from django.db import models
from django.utils import timezone
import uuid

class DeviceProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    created_date = models.DateField(default=timezone.now)
    created_time = models.TimeField(default=timezone.now)
    entity_type = models.CharField(max_length=50, default='DEVICE_PROFILE')

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'deviceprofile'
