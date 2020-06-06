from django.urls import path
from . import views
urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('signup', views.sign_up, name='sign_up'),
    path('login', views.loginpage, name='login'),
    path('logout', views.logoutpage, name='logout'),
    path('dashbord/customer', views.customer, name='customer'),
    path('dashbord/rooms', views.room, name='rooms'),
    path('dashbord', views.dashbord, name='dashbord'),
    path('dashbord/rooms/available', views.available, name='available'),
    path('dashbord/rooms/available/updatetime/<str:pk>', views.updatetime, name='updatetime'),
    path('dashbord/rooms/CreateRoom', views.CreateRoom, name='CreateRoom'),
    path('dashbord/rooms/UpdateRoom/<str:Room_id>/', views.UpdateRoom, name='UpdateRoom'),
    path('dashbord/rooms/DeleteRoom/<str:pk>/', views.DeleteRoom, name='DeleteRoom'),
    path('dashbord/rooms/RoomBooking/', views.RoomBooking, name='RoomBooking'),
    path('dashbord/rooms/RoomBooking/Reservation/<str:pk>/', views.reservation, name='Reservation'),
    path('dashbord/myprofile', views.myprofile, name='myprofile'),

]
