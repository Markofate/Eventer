from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Users(AbstractUser):
    REQUIRED_FIELDS = []
    user_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    password = models.TextField(max_length=20)