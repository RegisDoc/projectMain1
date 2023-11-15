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


def homepage(request):
    search_query = request.GET.get("q", "")
    cars = Car.objects.all()

    if search_query:
        cars = cars.filter(model__icontains=search_query)

    context = {
        "cars": cars,
        "search_query": search_query,
    }

    return render(request, "app/homepage.html", context)
