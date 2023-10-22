from django.db import models
import uuid
from django.contrib.auth.models import User
from django.conf import settings



class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


# Create your models here.
class Item(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description  = models.CharField(max_length=1000)
    image = models.TextField(max_length=1000)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)




