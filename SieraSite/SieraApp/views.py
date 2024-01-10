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
    if request.method == "POST":
       
        fullname_ = request.POST["fullname"]
        phone_ = request.POST["phone"]
        email_= request.POST["email"]
        pickup_ = request.POST["pickup"]
        pickupHour_ =  request.POST["pickupHour"]
        dropoff_ =request.POST["dropoff"] 
        dropoffHour_ = request.POST["dropoffHour"]
        Order( car=carInfo,fullname=fullname_, phone=phone_, email=email_, pick_day=pickup_, pick_time=pickupHour_, drop_day=dropoff_, drop_time=dropoffHour_).save()
    return render(request, "carDetail.html",context)


def myReservation(request):
    myReservations = Order.objects.all()
    context = {"myReservations": myReservations}
    return render(request, "myReservation.html", context)






