from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import Cart,Order
from items.serializers import ProductSerializer

class OrderSerializer(serializers.ModelSerializer):
   # author_username = serializers.CharField(source='author.username')
   class Meta:
       model = Order
       fields = ('id','invoice_number','cart','client', 'driver','cart_sale_price','created_at','completed_at' )


class CartSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    class Meta:
           model = Cart
           fields = "__all__"
