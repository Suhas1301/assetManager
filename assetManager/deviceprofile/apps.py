from django.apps import AppConfig


class DeviceprofileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'deviceprofile'

    def ready(self):
        import deviceprofile.signals
