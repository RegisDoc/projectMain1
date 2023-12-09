from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("cars/", views.cars, name="cars"),
    path("contact/", views.contact, name="contact"),
    path("myReservation/", views.myReservation, name="myReservation"),
    path("carDetail/<id>",views.carDetail, name="carDetail")

]