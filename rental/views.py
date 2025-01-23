from django.shortcuts import render, redirect
from django.http import HttpResponse
import random

# Sample car data
cars = [
    {"id": 1, "name": "Corolla", "type": "Sedan", "price": 2000},
    {"id": 2, "name": "BMW", "type": "Sedan", "price": 7000},
    {"id": 3, "name": "NOAH", "type": "Mini Van", "price": 3500},
    {"id": 4, "name": "NOAH-X", "type": "Mini Van", "price": 4000},
    {"id": 5, "name": "VOXY", "type": "Mini Van", "price": 4000},
    {"id": 6, "name": "HIACE", "type": "Van", "price": 4500},
    {"id": 7, "name": "H1", "type": "Van", "price": 5000},
    {"id": 8, "name": "Pajero", "type": "SUV", "price": 16000},
]

bookings = []  # Store bookings

# Car List View
def car_list(request):
    return render(request, 'rental/car_list.html', {"cars": cars})
# Contact page
def contact(request):
    return render(request, 'rental/contact.html')

# Booking Form View
def booking_form(request, car_id):
    selected_car = next((car for car in cars if car["id"] == car_id), None)
    if not selected_car:
        return HttpResponse("Car not found", status=404)

    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        duration = int(request.POST.get('duration', 0))
        token = random.randint(100000, 150000)
        total_amount = selected_car['price'] * duration

        booking = {
            "car": selected_car,
            "name": name,
            "phone": phone,
            "email": email,
            "duration": duration,
            "total_amount": total_amount,
            "token": token
        }
        bookings.append(booking)
        return redirect('confirmation')

    return render(request, 'rental/booking_form.html', {"car": selected_car})

# Confirmation View
def confirmation(request):
    if not bookings:
        return HttpResponse("No booking found", status=404)

    booking = bookings[-1]  # Get the latest booking
    return render(request, 'rental/confirmation.html', {"booking": booking})

# Return Login View
def return_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'Admin' and password == 'admin':
            return redirect('return_car')
        else:
            return HttpResponse("Invalid login credentials.")

    return render(request, 'rental/login.html')

# Return Car View
def return_car(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        token = int(request.POST.get('token', 0))

        for booking in bookings:
            if booking["phone"] == phone and booking["token"] == token:
                bookings.remove(booking)
                return HttpResponse("Car returned successfully.")

        return HttpResponse("Invalid phone or token.", status=400)

    return render(request, 'rental/return_car.html')

# About Us View
def about_us(request):
    return render(request, 'rental/about_us.html')
