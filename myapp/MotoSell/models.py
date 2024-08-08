from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator

class Vehicle(models.Model):
    MOTORCYCLE = 'motocykl'
    PASSENGER_CAR = 'osobowy'
    TRUCK = 'ciężarowy'
    VEHICLE_CATEGORY_CHOICES = [
        (MOTORCYCLE, 'Motocykl'),
        (PASSENGER_CAR, 'Osobowy'),
        (TRUCK, 'Ciężarowy'),
    ]

    PETROL = 'benzyna'
    DIESEL = 'diesel'
    LPG = 'LPG'
    FUEL_TYPE_CHOICES = [
        (PETROL, 'Benzyna'),
        (DIESEL, 'Diesel'),
        (LPG, 'LPG'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=VEHICLE_CATEGORY_CHOICES)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField(
        validators=[MaxValueValidator(2025)]  # Year should not exceed 2025
    )
    mileage = models.PositiveIntegerField(
        validators=[MaxValueValidator(1500000)]  # Mileage should not exceed 1.5 million
    )
    engine_capacity = models.PositiveIntegerField(
        validators=[MaxValueValidator(20)]  # Engine capacity should not exceed 20
    )
    power = models.PositiveIntegerField(
        validators=[MaxValueValidator(2000)]  # Power should not exceed 2000
    )
    fuel_type = models.CharField(max_length=10, choices=FUEL_TYPE_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='vehicles_photos/')
    date_added = models.DateField(auto_now_add=True)
    date_published = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"
