from django.shortcuts import render
from .models import User,Image,Album
from rest_framework import viewsets, generics

from .serializers import AlbumSerializers,ImageSerializers



###Albums

class AlbumViewSet(viewsets.ModelViewSet):
    pass


class ImageViewset(viewsets.ModelViewSet):
    pass
