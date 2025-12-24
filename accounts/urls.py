from django.urls import path
from .views import Login,Signup,UserDetailUpdateView


urlpatterns = [
    path('login/',Login.as_view()),
    path('signup/',Signup.as_view()),
    path('me/',UserDetailUpdateView.as_view()),
]