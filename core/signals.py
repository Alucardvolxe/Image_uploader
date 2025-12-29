from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from core.models import Image
from django.core.cache import cache


@receiver([post_save,post_delete], sender=Image)
def invalidate_Image_cache(sender,instance,**kwargs):
    """Invalidate Image list chache when an image is uploaded updated or deleted"""
    print("clearing product cache")


    cache.delete_pattern('*image_list','*album_list')