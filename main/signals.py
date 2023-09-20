from django.db.models.signals import pre_delete
from django.dispatch import receiver
from .models import Item
import os


@receiver(pre_delete, sender=Item)
def delete_item_images(sender, instance, **kwargs):
    try:
        os.remove(instance.image.path)
    except Exception as e:
        print(e)
