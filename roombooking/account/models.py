from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.conf import settings
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model

User=get_user_model()
# Create your models here.
class Room(models.Model):
    CATEGORY=(
    ('single','single'),
    ('double','double'),
    ('king','king'),
    ('queen','queen')
    )

    list_status=(
    ('Booked','Booked'),
    ('Unbooked','Unbooked')
    )
    Category= models.CharField(max_length=200,choices=CATEGORY)
    description=models.CharField(max_length=200)
    price=models.FloatField()
    date=models.DateTimeField(auto_now_add=True,null=True)
    #Room_status=models.CharField(max_length=10,choices=list_status,null=True)
    #Room_no=models.IntegerField(max_length=5,null=True)
    def get_price(self):
        return self.price

    def __str__(self):
        return self.Category


class Reservation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    room = models.ForeignKey(Room,null=True,on_delete=models.CASCADE)
    guestFirstName = models.CharField(max_length  = 255)
    guestLastName = models.CharField(max_length  = 255)
    CheckIn = models.DateField(default=timezone.now,null=True)
    CheckOut = models.DateField(default=timezone.now,null=True)
    status=models.CharField(max_length=10,default='UnBooked',null=True)

    def __str__(self):
        return self.room.Category


class Customer(models.Model):
    room = models.ForeignKey(Room,null=True,on_delete=models.CASCADE)
    name= models.CharField(max_length=200,null=True)
    email= models.CharField(max_length=200,null=True)
    Phone=models.CharField(max_length=20,null=True)
    date=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name


class Available(models.Model):
    Advance_Booking_Days=models.IntegerField(null=True)
    Time_For_available=models.TimeField(default=timezone.now,null=True)
    Time_up_to_available=models.TimeField(default=timezone.now,null=True)


class profile(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    #room = models.ForeignKey(Room,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

def post_save_profile_create(sender, instance, created, *args, **kwargs):
    if created:
        profile.objects.get_or_create(user=instance)

post_save.connect(post_save_profile_create, sender=settings.AUTH_USER_MODEL)
