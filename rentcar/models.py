from django.db import models
from django.contrib.auth.models import User

class Car(models.Model):
    GEAR_OPTIONS = (
        ("A", "Automatic"),
        ("M", "Manuel"),
        ("H", "Hybrid"),
    )
    plate_number = models.CharField(max_length=15)
    brand = models.CharField(max_length=15)
    model = models.CharField(max_length=15)
    year = models.PositiveSmallIntegerField()
    gear = models.CharField(max_length=10, choices=GEAR_OPTIONS)
    rent_per_day = models.IntegerField()
    availability = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.brand} {self.model}"

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.IntegerField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

class Reservation(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="car_reservation")
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="customer_reservation")

    def __str__(self):
        return f"{self.customer}'s Reservation"

