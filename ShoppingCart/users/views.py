from django.shortcuts import render,get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .serializers import UserSerializer,RegisterSerializer
from django.contrib.auth.models import User
from django.contrib.auth import login,logout
# Create your views here.

class RegisterUserAPI(generics.CreateAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = '/dashboard/signup.html'
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class ListAllUsersAPI(generics.ListAPIView):
    authentication_classes = [SessionAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class UpdateUserAPI(generics.UpdateAPIView):
    authentication_classes = [SessionAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

  

class DeleteUserAPI(generics.DestroyAPIView):
    authentication_classes = [SessionAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer


    

