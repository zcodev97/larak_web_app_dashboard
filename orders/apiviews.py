from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from .models import Book, Author,BooksRating, User
from .serializers import  UserSerializer,OrderSerializer,CartSerializer
from rest_framework.permissions import IsAuthenticated,DjangoModelPermissions
from rest_framework_simplejwt.tokens import RefreshToken


class LoginView(APIView):
   permission_classes = ()
   def post(self,request):
       username = request.data.get('username')
       password = request.data.get('password')
       user = authenticate(username=username,password= password)
       if user:
           token = RefreshToken.for_user(user)
           return Response({'token': token.access_token})
       else:
           return Response({'error' : "wrong Credentials"}, status=status.HTTP_401_UNAUTHORIZED)



class UserCreate(generics.CreateAPIView):
   authentication_classes = ()
   permission_classes = ()
   serializer_class = UserSerializer

class UserCreate(generics.CreateAPIView):
   authentication_classes = ()
   permission_classes = ()
   serializer_class = UserSerializer

class UsersList(generics.ListCreateAPIView):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [IsAuthenticated, DjangoModelPermissions]

class UserDetails(generics.RetrieveDestroyAPIView):
   queryset = User.objects.all()
   serializer_class = UserSerializer

class Records(generics.ListCreateAPIView):
   queryset = Record.objects.all()
   serializer_class = RecordSerilzer
   permission_classes = [IsAuthenticated,DjangoModelPermissions]