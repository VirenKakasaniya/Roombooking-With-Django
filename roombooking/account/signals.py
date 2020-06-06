from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Customer

def create_profile(sender,instance,created,**kwarg):
    if created:
        print('profile created')

post_save.connect(create_profile,sender=User)
