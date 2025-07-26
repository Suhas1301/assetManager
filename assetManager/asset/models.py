from django.db import models
from django.utils import timezone
import uuid

class Asset(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    created_date = models.DateField(default=timezone.now)
    created_time = models.TimeField(default=timezone.now)
    entity_type = models.CharField(max_length=50, default='ASSET')
    asset_profile = models.ForeignKey('assetprofile.AssetProfile', on_delete=models.CASCADE, related_name='assets', null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'asset'
