from django.shortcuts import render

# Create your views here.
from .models import User
from .serializers import UserSerializer,LoginSerializer,SignupSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken,AccessToken

class Signup(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignupSerializer
    permission_classes =[AllowAny]
           


class Login(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]
    def post(self,request,*args,**kwarks):
        username = request.data.get('username')
        password = request.data.get('password')
        user=authenticate(username =username, password=password)


        if user is not None:
            refresh = RefreshToken.for_user(user)
            user_serializer = UserSerializer(user)
            return Response(
                {
                    'refresh':str(refresh),
                    'access':str(refresh.access_token),
                    'user':user_serializer.data

                }
            )
        else:
            return Response(
                {'detail':'user not found'}
            )
        

            
        