from django.db import models
from django.core.validators import *
from django.contrib.auth.models import User
# Create your models here.


class Location(models.Model):
    city = models.CharField(max_length=50, null=True, blank=True)
 
    def __str__(self):
        return self.city
 
class CarDealer(models.Model):
    car_dealer = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    phone =  models.CharField(validators = [MinLengthValidator(10), MaxLengthValidator(10)], max_length = 10, null=True, blank=True)
    location = models.OneToOneField(Location, on_delete=models.PROTECT, null=True, blank=True)
    earnings = models.IntegerField(default=0, null=True, blank=True)
    type = models.CharField(max_length=20, blank=True, null=True)
 
    def __str__(self):
        return str(self.car_dealer)
 
class Car(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(upload_to="", null=True, blank=True)
    car_dealer = models.ForeignKey(CarDealer, on_delete=models.PROTECT, null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)
    is_available = models.BooleanField(default=True,null=True, blank=True)
    rent = models.CharField(max_length=10, blank=True, null=True)
    price = models.DecimalField(max_digits = 3, decimal_places=0, null=True, blank=True)
    year=  models.DecimalField(max_digits = 4, decimal_places=0, null=True, blank=True)
    engine = models.CharField(max_length=50, null=True, blank=True)
    transmission = models.CharField(max_length=150, null=True, blank=True)
    include = models.CharField(max_length=250, null=True, blank=True)
 
    def __str__(self):
        return self.name
 
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    phone = models.CharField(validators = [MinLengthValidator(10), MaxLengthValidator(10)], max_length = 10, null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)
    type  = models.CharField(max_length=20, blank=True, null=True)
 
    def __str__(self):
        return str(self.user)
 
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    car_dealer = models.ForeignKey(CarDealer, on_delete=models.CASCADE, null=True, blank=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True, blank=True)
    rent = models.CharField(max_length=10, null=True, blank=True)
    days = models.CharField(max_length=3, null=True, blank=True)
    is_complete = models.BooleanField(default=False, null=True, blank=True)




#   from datetime import datetime, timedelta

class CarRental(models.Model):
    def __init__(self, daily_rate, hourly_rate,):
        self.daily_rate = daily_rate
        self.hourly_rate = hourly_rate
        

    def calculate_rental_cost(self, start_time, end_time):
        
        rental_duration = end_time - start_time
        days = rental_duration.days
        hours = rental_duration.seconds // 3600

        total_cost = (self.daily_rate * days) + (self.hourly_rate * hours) 

        

        return total_cost

# rental_agency = CarRental(daily_rate=50, hourly_rate=10)

# print(f'Total Rental Cost: ${total_cost:.2f}')
