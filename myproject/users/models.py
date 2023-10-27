from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from datetime import timezone
from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class Systems(models.Model):
    name = models.CharField(max_length=100, null=False, blank=True)
    description = models.CharField(max_length=200   , blank=True, null=False)
    url = models.CharField(max_length=100, null = False, blank=True)
    image = models.ImageField(upload_to='media/', blank=True, null=True)
    active = models.BooleanField(default=True)
    icon = models.CharField(max_length=150, null=False, blank=True)
    
    def __str__(self) -> str:
        return  self.name


class Roles(models.Model):
    role_name = models.CharField(max_length=150)

    def __str__(self):
        return self.role_name



    
    
    
class UsersSystem(models.Model):
    users_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    system_id = models.ForeignKey(Systems, on_delete=models.CASCADE, null=True, blank=True)


class UsersRole(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    role_id = models.ForeignKey(Roles, on_delete=models.CASCADE, null=True,blank=True)
