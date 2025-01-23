from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.car_list, name='car_list'),
    path('book/<int:car_id>/', views.booking_form, name='booking_form'),
    path('confirm/', views.confirmation, name='confirmation'),
    path('home/return/login/', views.return_login, name='return_login'),
    path('return/car/', views.return_car, name='return_car'),
    path('about/', views.about_us, name='about_us'),
    path('contact/', views.contact, name='contact'),
]