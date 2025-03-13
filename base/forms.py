from django.forms import ModelForm 
from .models import CustomUser,Booking
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.CharField(required=True,help_text='Required.Enter a valid email.')
    avatar = forms.ImageField(required=False)
    class Meta:
        model = CustomUser
        fields = ('username','password1', 'password2','email')



class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["latitude", "longitude","description","service_type"]
        widgets = {
            "latitude": forms.HiddenInput(),
            "longitude": forms.HiddenInput(),
            "service_type": forms.HiddenInput(),
        }
