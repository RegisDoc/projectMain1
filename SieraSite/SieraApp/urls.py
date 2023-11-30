from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("cars/", views.cars, name="cars"),
    path("contact/", views.contact, name="contact"),
    path("rental/", views.rental, name="rental"),
    path("carDetail/<id>",views.carDetail, name="carDetail")

]