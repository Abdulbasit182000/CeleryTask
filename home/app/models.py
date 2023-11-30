from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager

#Testing Celery
class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

class CustomUser(AbstractUser):
    username= models.CharField(max_length=150,default='abdul')
    email= models.EmailField(unique=True)
    contact = models.CharField(max_length=100, blank=True, null=True)
    date_of_birth = models.DateTimeField(blank=True, null=True)

    objects=UserManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username']


    def __str__(self):
        return self.email