from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    phone=models.CharField(max_length=15,blank=True,null=True,unique=True)
    email=models.EmailField(blank=True,null=True,unique=True)
    username=models.CharField(max_length=100,blank=False,null=False,unique=True)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=False)
    date_joined=models.DateTimeField(auto_now_add=True)
    last_login=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.username}'