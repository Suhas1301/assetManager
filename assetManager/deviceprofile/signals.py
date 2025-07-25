# deviceprofile/signals.py
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import DeviceProfile

@receiver(post_migrate)
def create_default_device_profile(sender, **kwargs):
    if not DeviceProfile.objects.filter(name='default').exists():
        DeviceProfile.objects.create(
            name='default',
        )
