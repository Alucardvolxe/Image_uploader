from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from core.models import Image
from django.core.cache import cache


@receiver([post_save,post_delete], sender=Image)
def invalidate_Image_cache(sender,instance,**kwargs):

    print("clearing image cache")


    version = cache.get("image_list_version", 1)
    cache.set("image_list_version", version + 1)