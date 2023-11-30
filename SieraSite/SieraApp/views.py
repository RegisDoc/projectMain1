from django.shortcuts import render, HttpResponse
from .models import *
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




# def homepage(request):
#     search_query = request.GET.get("q", "")
#     cars = Car.objects.all()

#     if search_query:
#         cars = cars.filter(model__icontains=search_query)

#     context = {
#         "cars": cars,
#         "search_query": search_query,
#     }

#     return render(request, "app/homepage.html", context)
