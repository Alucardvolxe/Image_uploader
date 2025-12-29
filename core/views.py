from django.shortcuts import render
from .models import User,Image,Album
from rest_framework import viewsets, generics
from .permissions import isOwnerOrAdmin
from .serializers import AlbumSerializers,ImageSerializers
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie, vary_on_headers
from django.utils.decorators import method_decorator
from .filters import ImageFilterSet, AlbumFilterSet
from django_filters.rest_framework import DjangoFilterBackend
###Albums

class AlbumViewSet(viewsets.ModelViewSet):
    queryset=Album.objects.all()
    serializer_class= AlbumSerializers
    permission_classes = [isOwnerOrAdmin, IsAuthenticated]
    filter_backends =[DjangoFilterBackend]
    filterset_class = AlbumFilterSet
    @method_decorator(cache_page(60 * 5 , key_prefix="albumpppppp  _list"))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    




class ImageViewset(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class=ImageSerializers
    permission_classes = [isOwnerOrAdmin, IsAuthenticated]
    filter_backends =[DjangoFilterBackend]
    filterset_class = ImageFilterSet
    @method_decorator(cache_page(60 * 5 , key_prefix="image_list"))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def get_queryset(self):
        import time
        time.sleep(2)

        user = self.request.user
        
        if user.is_staff:
            return Image.objects.all()
        
        return Image.objects.filter(Q(visibilty = "Public")|Q(visibilty = "Private", user = user))
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
