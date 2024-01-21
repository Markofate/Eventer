from django.db import models
from user.models import Users

# Create your models here.
class Location(models.Model):
    location_id = models.AutoField(primary_key=True)
    location_name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.location_name

class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=255)
    description = models.TextField()
    event_date = models.DateField()
    event_time = models.TimeField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE,null=True, blank=True)
    event_img = models.ImageField(null=True, upload_to="images/", unique=False)
    creator = models.ForeignKey(Users,on_delete=models.CASCADE, null=True, blank=True)
    

    def __str__(self):
        return self.event_name     
