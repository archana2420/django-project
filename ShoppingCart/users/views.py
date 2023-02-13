from django.shortcuts import render,get_object_or_404,redirect,HttpResponse
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .serializers import UserSerializer,RegisterSerializer
from django.contrib.auth.models import User
from django.contrib.auth import login,logout
from rest_framework.views import APIView
# Create your views here.

class RegisterUserAPI(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'dashboard/sign_up.html'
    

    def get(self,request):
        serializer = RegisterSerializer()
        return Response({'serializer':serializer})

    def post(self, request):
        print(request.data)
        serializer = RegisterSerializer(data=request.data)
       
        if not serializer.is_valid():
            return Response({'serializer': serializer})
        serializer.save()
        return redirect('login')


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


    

