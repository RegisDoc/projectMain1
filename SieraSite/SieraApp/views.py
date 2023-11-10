from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request,"home.html")
def about(request):
    return render(request,"about.html")
def cars(request):
    return render(request,"cars.html")
def contact(request):
    return render(request,"contact.html")
def rental(request):
    return render(request,"rental.html")

