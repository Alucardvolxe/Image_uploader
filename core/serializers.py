from rest_framework import serializers
from .models import Image,Album




class ImageSerializers(serializers.ModelSerializer):
    album_name = serializers.CharField(
        source = 'album.name',
        read_only =True
    )
    class Meta:
        models= Image
        fields = ("title","url","description","visibilty","album_name")




class AlbumSerializers(serializers.ModelSerializer):
    
    images = ImageSerializers(many=True,read_only=True)
    class Meta:
        model = Album
        fields = ('name',"images")

        
    def validate_name(self,value):
        if Album.objects.filter(name=value).exists():
            raise serializers.ValidationError(
                {"Error":"An album with this name already exists"}
            )
        return value