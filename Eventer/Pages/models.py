from django.db import models

# Create your models here.
class Location(models.Model):
    location_id = models.IntegerField(primary_key=True)
    location_name = models.CharField(max_length=255)

class Event(models.Model):
    event_id = models.IntegerField(primary_key=True)
    event_name = models.CharField(max_length=255)
    description = models.TextField()
    event_date = models.DateField()
    event_time = models.TimeField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    username = models.CharField(max_length=50)