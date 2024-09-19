from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'


class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to='pics')
    
    def __str__(self):
        return self.name