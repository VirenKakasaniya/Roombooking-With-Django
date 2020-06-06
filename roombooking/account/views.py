from django.contrib.auth.models import User,auth,Group
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .decorators import unauthenticate_user,allowed_user
import datetime
from django.utils import timezone
from django.contrib.auth.decorators import login_required


# Create your views here.


def home_page(request):
    return render(request,'account/index.html')

def sign_up(request):
    form=CreateUserForm()

    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            username=form.cleaned_data.get('username')
            staff=form.cleaned_data.get('is_staff')
            if staff==True:
                group=Group.objects.get(name='Manager')
            else:
                group=Group.objects.get(name='customer')
            user.groups.add(group)
            messages.success(request,'account was created for '+username)
            return redirect('login')
    context={'form':form}
    return render(request,'account/signup.html',context)

@unauthenticate_user
def loginpage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('dashbord')
        else:
            messages.info(request,'username or password incorrect')


    context={}
    return render(request,'account/login.html',context)



def logoutpage(request):
    logout(request)
    return redirect('login')

#@allowed_user(allowed_roles=['Manager'])
def dashbord(request):
    context={}
    return render(request,'account/home.html',context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['Manager'])
def customer(request):
    customers = Customer.objects.all()
    #rooms=Room.objects.all()
    context={'customers':customers}
    return render(request,'account/customer.html',context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['Manager'])
def room(request):
    rooms=Room.objects.all()
    context={'rooms':rooms}
    return render(request,'account/rooms.html',context)
#@allowed_user(allowed_roles=['Manager'])
def CreateRoom(request):
    form=CreateRoomForm()
    if request.method=='POST':
        form=CreateRoomForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('rooms')
    context={'form':form}
    return render(request,'account/createroom.html',context)

#@allowed_user(allowed_roles=['Manager'])
def UpdateRoom(request,Room_id):
    room=Room.objects.get(id=Room_id)
    form=CreateRoomForm(instance=room)
    if request.method=='POST':
        form=CreateRoomForm(request.POST,instance=room)
        if form.is_valid:
            form.save()

    context={'form':form}
    return render(request,'account/createroom.html',context)
#@allowed_user(allowed_roles=['Manager'])
def DeleteRoom(request,pk):
    room=Room.objects.get(id=pk)
    if request.method=='POST':
        room.delete()
        return redirect('rooms')
    context={'room':room}
    return render(request,'account/delete.html',context)


def available(request):
    time=Available.objects.all()
    context={'time':time}
    return render(request,'account/available.html',context)

def updatetime(request,pk):
    time=Available.objects.get(id=pk)
    form=AvailableForm(instance=time)
    if request.method=='POST':
        form=AvailableForm(request.POST,instance=time)
        if form.is_valid:
            form.save()
            return redirect('available')

    context={'form':form}
    return render(request,'account/updatetime.html',context)



def RoomBooking(request):
    rooms=Room.objects.all()
    context={'rooms':rooms}
    return render(request,'account/roombooking.html',context)

@login_required(login_url='login')
def reservation(request,pk):
    if request.method=='POST':
        if pk:
            room=Room.objects.get(pk=pk)
            guestFirst_Name=request.POST.get('guestFirstName')
            guestLast_Name=request.POST.get('guestLastName')
            email=request.POST.get('email')
            phone=request.POST.get('phone')
            check_in=request.POST.get('checkin')
            check_out=request.POST.get('checkout')
            start_date = datetime.date(int(check_in[0:4]),int(check_in[5:7]),int(check_in[8:10]))
            end_date = datetime.date(int(check_out[0:4]),int(check_out[5:7]),int(check_out[8:10]))

            if  (start_date-datetime.date.today()).days>10:
                return HttpResponse('<h1>you are too early!!!<h1>')

            filter_params = dict(CheckIn__lte=end_date, CheckOut__gte=start_date)
            is_occupied = Reservation.objects.filter(**filter_params, room=room).exists()

            if is_occupied:
                return HttpResponse('<h1>This room is already booked<h1>')

            reservation=Reservation(user=request.user,room=room,guestFirstName=guestFirst_Name,
            guestLastName=guestLast_Name,CheckIn=check_in,CheckOut=check_out,status='Booked')
            reservation.save()
            customer=Customer(room=room,name=guestFirst_Name,email=email,Phone=phone)
            customer.save()
            timedeltaSum = end_date - start_date
            StayDuration = timedeltaSum.days
            print(type(StayDuration))
            price = room.get_price()
            context={'StayDuration':StayDuration,'room':room,'check_in':check_in,'check_out':check_out,'price':price}
            return render(request,'account/invoice.html',context)
    context={}
    return render(request,'account/reservation.html',context)

def myprofile(request):
    my_user_profile=profile.objects.filter(user=request.user).first()
    my_booking=Reservation.objects.filter(user=request.user).first()

    context={'my_user_profile':my_user_profile,'my_booking':my_booking}
    return render(request,'account/profile.html',context)
