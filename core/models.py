from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from django.conf import settings



class UserType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
class User(AbstractUser):
    email = models.EmailField(unique=True)
    user_type = models.ForeignKey(UserType,on_delete=models.CASCADE)


