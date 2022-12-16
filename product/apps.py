from django.apps import AppConfig
from django.db.models.signals import pre_save


class ProductConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'product'

    def ready(self):
        from . import signals
        
