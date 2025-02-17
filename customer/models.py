from django.db import models
from django.contrib.auth.models import AbstractUser

class Customer(AbstractUser):
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)