import django_filters
from .models import Image,Album


class ImageFilterSet(django_filters.FilterSet):
    

    class Meta:
        model = Image
        fields = {
            'title':['iexact','exact'],
            'visibilty':['exact'],
            

        }

class AlbumFilterSet(django_filters.FilterSet):
    class Meta:
        model = Album
        fields = {
            'name':['iexact']
        }