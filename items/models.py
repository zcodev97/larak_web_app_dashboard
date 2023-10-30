from django.db import models
import uuid
from django.contrib.auth.models import User




class Size(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    # amount = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sku =  models.CharField(max_length=255)
    barcode = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description  = models.CharField(max_length=1000)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    image = models.TextField(max_length=1000)
    in_stock = models.IntegerField()
    cost = models.FloatField(max_length=100)
    sale_price = models.FloatField(max_length=100)
    size = models.ForeignKey(Size,on_delete=models.CASCADE)
    status = models.BooleanField()
    created_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Finance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    invoice_number = models.CharField(max_length=255)
    cart_cost_price = models.FloatField(max_length=100)
    cart_sale_price = models.FloatField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)


class Banner(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.CharField(max_length=255)
    to_product = models.ForeignKey(Product,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
