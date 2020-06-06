from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django import forms

class CreateRoomForm(ModelForm):
    class Meta:
        model=Room
        fields = '__all__'



class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2','is_staff']
        #fields = '__all__'


class ReservationForm(ModelForm):
    class Meta:
        model=Reservation
        fields=['guestFirstName','guestLastName','CheckIn','CheckOut']
        #fields = '__all__'


class AvailableForm(ModelForm):
    class Meta:
        model=Available
        fields='__all__'
