from django.db.models.signals import post_save
from django.dispatch import receiver

from product.models import Product
from product.services import convert_image


@receiver(post_save, sender=Product)
def pre_save_dispatcher(sender, instance, **kwargs):
    convert_image(instance.image.name)


