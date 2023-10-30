from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import Product,Category,Finance,Size,Banner


class ProductSerializer(serializers.ModelSerializer):
   # author_username = serializers.CharField(source='author.username')
   class Meta:
       model = Product
       fields = "__all__"

