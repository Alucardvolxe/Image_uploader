from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email']



class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username','password']
        

class SignupSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)


    class Meta:
        model = User
        fields = ['username','email','password']


    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


    def validate_username(self,value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError(
                {'error':'username already exists'}
            )
        return value

    def validate_email(self,value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                {'error':'email already exists'}
            )#
        return value
    

class user_update_serializer(serializers.ModelSerializer):
    
    class meta:
        model = User
        fields = ("username","password","email")

    def update(self, instance, validated_data):
        password = validated_data.pop("password",None)
        for attr, value in validated_data.items():
            setattr(instance,attr,value)
        if password:
            instance.set_password(password)

        instance.save()
        return instance