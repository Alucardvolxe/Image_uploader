from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import AlbumViewSet,ImageViewset
urlpatterns=[
    
]

routers = DefaultRouter()
routers.register("albums", AlbumViewSet)
routers.register("Images", ImageViewset)

urlpatterns+= routers.urls