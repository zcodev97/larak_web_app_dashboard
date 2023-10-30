from django.db import models
from django.contrib.auth.models import User
import uuid
from items.models import Product
class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # cart_items = models.ManyToManyField(Product)
    cart_items = models.ManyToManyField(Product, related_name='carts')
    created_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    invoice_number = models.CharField(max_length=255)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    client = models.ForeignKey(User, on_delete=models.CASCADE,related_name='client')
    driver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='driver')
    cart_cost_price = models.FloatField(max_length=100)
    cart_sale_price = models.FloatField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)
    completed_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.cart.cart_items
    # title = models.ForeignKey(Items,on_delete=models.CASCADE)

