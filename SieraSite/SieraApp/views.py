from django.shortcuts import render, HttpResponse
from .models import *
from datetime import datetime
# Create your views here.
def home(request):
    cars = Car.objects.all()
    context = {"cars":cars}
    return render(request,"home.html",context)
def about(request):
    return render(request,"about.html")
def cars(request):
    cars = Car.objects.all()
    context = {"cars":cars}
    return render(request,"cars.html", context)
def contact(request):
    return render(request,"contact.html")
def rental(request):
    return render(request,"rental.html")
def carDetail(request,id):
    carInfo = Car.objects.get(pk=id)
    context = {"carInfo":carInfo}
    return render(request, "carDetail.html",context)
def myReservation (request):
    myReservation = CarRental.objects.all()
    context = {"myReservation": CarRental}
    return render(request, "myReservation.html", context)



# to calculate the booking process

# def calculate_booking_duration(start_date_str, end_date_str):
#     # Convert date strings to datetime objects
#     start_date = datetime.strptime(start_date_str, '%Y-%m-%d %H:%M:%S')
#     end_date = datetime.strptime(end_date_str, '%Y-%m-%d %H:%M:%S')

#     # Calculate the difference between dates
#     duration = end_date - start_date

#     # Extract days and seconds from the duration
#     days = duration.days
#     seconds = duration.seconds

#     # Calculate hours from seconds
#     hours = seconds // 3600

#     return days, hours





