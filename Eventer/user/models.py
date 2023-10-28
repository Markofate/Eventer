from django.db import models

# Create your models here.


class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    username = models.CharField(max_length=50)
    password = models.TextField(max_length=20)