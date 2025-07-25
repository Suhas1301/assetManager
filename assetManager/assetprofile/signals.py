# assetprofile/signals.py
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import AssetProfile

@receiver(post_migrate)
def create_default_asset_profile(sender, **kwargs):
    if not AssetProfile.objects.filter(name='default').exists():
        AssetProfile.objects.create(
            name='default',
        )
