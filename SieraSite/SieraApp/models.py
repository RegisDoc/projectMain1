from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class CarManager(models.Manager):
    def create_car(self, model, price_per_hour, image):
        car = self.model(model=model, price_per_hour=price_per_hour, image=image)
        car.save()
        return car

 class Car(models.Model):
    model = models.CharField(max_length=100)
    price_per_hour = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='image')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    is_rented = models.BooleanField(default=False)
    