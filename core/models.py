from django.db import models

from accounts.models import User


class Album(models.Model):
    name = models.CharField(max_length=200, unique=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Image(models.Model):
    class VISIBLITY_OPTION(models.TextChoices):
        PUBLIC = "Public"
        PRIVATE = "Private"

    title = models.CharField(max_length=200,unique=True)
    img_url = models.URLField(default="")
    description = models.CharField()
    visibilty = models.CharField(max_length=20, choices=VISIBLITY_OPTION,default=VISIBLITY_OPTION.PUBLIC)
    album = models.ForeignKey(Album,related_name="images", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title
