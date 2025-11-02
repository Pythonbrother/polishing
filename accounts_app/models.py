from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    username = models.CharField(unique=False)
    email = models.EmailField(unique=True)
    gender = models.CharField(choices=[('male','male'),('female','female')],null=True,blank=True,max_length=10)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username