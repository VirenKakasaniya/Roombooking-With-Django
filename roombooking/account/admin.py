from django.contrib import admin
from .models import *

class UserAdmin(admin.ModelAdmin):
    list_display=['name','email','Phone','date']




admin.site.register(Customer,UserAdmin)
admin.site.register(Room)
admin.site.register(Reservation)
admin.site.register(Available)
