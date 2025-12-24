from django.shortcuts import render
from .models import User,Image,Album
from rest_framework import viewsets, generics
from .permissions import isOwnerOrAdmin
from .serializers import AlbumSerializers,ImageSerializers
from django.db.models import Q


###Albums

class AlbumViewSet(viewsets.ModelViewSet):
    queryset=Album.objects.all()
    serializer_class= AlbumSerializers
    


class ImageViewset(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class=ImageSerializers
    permission_classes = [isOwnerOrAdmin]

    def get_queryset(self):
        user = self.request.user
        
        if user.is_staff:
            return Image.objects.all()
        
        return Image.objects.filter(Q(visibilty = "Public")|Q(visibilty = "Private"))
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
