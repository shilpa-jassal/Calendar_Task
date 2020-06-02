from django.db import models

# Create your models here.
class User(models.Model):
    username=models.CharField('User name',max_length=100)
    email=models.CharField('User email',max_length=100)
    password= models.CharField("User Password",max_length=200)