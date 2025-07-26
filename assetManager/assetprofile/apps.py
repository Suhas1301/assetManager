from django.apps import AppConfig


class AssetprofileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'assetprofile'

    def ready(self):
        import assetprofile.signals
