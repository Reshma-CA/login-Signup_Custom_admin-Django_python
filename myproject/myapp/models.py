from django.db import models

# Create your models here.
from django.core.exceptions import ValidationError

class Signup(models.Model):
    username=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    cpassword=models.CharField(max_length=200)
    phonenumber=models.CharField(max_length=200)
    address=models.CharField(max_length=400)

