from django.db import models
from django.contrib.auth.models import User
import uuid
from django.conf import settings
# from ..items import Items
# Create your models here.


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    invoice_number = models.CharField(max_length=255)
    client = models.CharField(max_length=255)
    driver = models.CharField(max_length=255)
    cart_cost_price = models.FloatField(max_length=100)
    cart_sale_price = models.FloatField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)
    completed_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    # title = models.ForeignKey(Items,on_delete=models.CASCADE)