from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from .models import Product
from .serializers import   ProductSerializer
from rest_framework.permissions import IsAuthenticated,DjangoModelPermissions
from rest_framework_simplejwt.tokens import RefreshToken

class ProductsList(generics.ListCreateAPIView):
   queryset = Product.objects.all()
   serializer_class = ProductSerializer
   permission_classes = [IsAuthenticated,DjangoModelPermissions]

class ProductDetails(generics.RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

