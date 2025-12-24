from rest_framework import serializers
from .models import Image,Album




class ImageSerializers(serializers.ModelSerializer):
    album = serializers.CharField(write_only=True)
    album_name = serializers.CharField(
        source = 'album.name',
        read_only =True
    )
    user = serializers.ReadOnlyField(source = "user.username")
    class Meta:
        model = Image
        fields = ("title","url","description","visibilty","album","album_name","user")

    def create(self, validated_data):
        album_name = validated_data.pop("album")
        album,created= Album.objects.get_or_create(name=album_name)
        image= Image.objects.create(
            album=album,
            **validated_data
        )
        return image



class AlbumSerializers(serializers.ModelSerializer):
    
    images = ImageSerializers(many=True,read_only=True)
    class Meta:
        model = Album
        fields = ('name',"images")

        
