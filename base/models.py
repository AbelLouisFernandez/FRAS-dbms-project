from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class CustomUser(AbstractUser):
    role = models.CharField(max_length=50)
    email = models.CharField(max_length=100, unique=True)  # Ensure email is unique

    def __str__(self):
        return self.username
    

class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    booked_at = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=100,default="Nothing",null=True)
    service_type = models.CharField(max_length=50,default="service")

    def __str__(self):
        return f"{self.user.username} - ({self.latitude}, {self.longitude})"

    