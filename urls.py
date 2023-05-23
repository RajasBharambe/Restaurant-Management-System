"""
URL configuration for restaurant_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from hotel.views import input_data, room_rent, hotel_bill_create, hotel_bill_success, restaurant_bill, laundry_bill, game_bill, display

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', input_data, name='input_data'),
    path('room_rent/', room_rent, name='room_rent'),
    path('hotel-bill/create/', hotel_bill_create, name='hotel_bill_create'),
    path('hotel-bill/success/', hotel_bill_success, name='hotel_bill_success'),
    path('restaurant_bill/', restaurant_bill, name='restaurant_bill'),
    path('laundry_bill/', laundry_bill, name='laundry_bill'),
    path('game_bill/', game_bill, name='game_bill'),
    path('display/', display, name='display'),
]
