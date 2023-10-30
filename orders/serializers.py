from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import Cart,User,Order

class UserSerializer(serializers.ModelSerializer):
   class Meta:
       model = User
       fields = ('username', 'email', 'password')
       extra_kwargs = {'password': {'write_only': True}}

   def create(self, validated_data):
       user = User(email=validated_data['email'], username=validated_data['username'])
       user.set_password(validated_data['password'])
       user.save()
       Token.objects.create(user=user)
       return user


class OrderSerializer(serializers.ModelSerializer):
   # author_username = serializers.CharField(source='author.username')
   class Meta:
       model = Order
       fields = "__all__"


class CartSerializer(serializers.ModelSerializer):
   class Meta:
       model = Cart
       fields = "__all__"
