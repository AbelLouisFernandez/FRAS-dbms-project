from django.contrib import admin
from .models import CustomUser,Booking
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Booking)
