from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from .models import Cart,Order
from .serializers import   OrderSerializer,CartSerializer
from rest_framework.permissions import IsAuthenticated,DjangoModelPermissions
from rest_framework_simplejwt.tokens import RefreshToken

class OrdersList(generics.ListCreateAPIView):
   queryset = Order.objects.all()
   serializer_class = OrderSerializer
   permission_classes = [IsAuthenticated,DjangoModelPermissions]

class OrderDetails(generics.RetrieveDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]


class CartsList(generics.ListCreateAPIView):
   queryset = Cart.objects.all()
   serializer_class = CartSerializer
   permission_classes = [IsAuthenticated,DjangoModelPermissions]

class CartDetails(generics.RetrieveDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

