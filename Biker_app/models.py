from django.db import models
from django.db import models
from django.utils import timezone

class Biker(models.Model):
    full_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=15)
    cnic = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=128)
    bike_model = models.CharField(max_length=100)
    vehicle_number = models.CharField(max_length=50)
    current_request_id = models.IntegerField(null=True, blank=True)
    joined_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.full_name} ({self.cnic})"

class BikerAvailability(models.Model):
    biker = models.ForeignKey(Biker, on_delete=models.CASCADE, related_name='availability')
    is_available = models.BooleanField(default=True)
    location_lat = models.FloatField()
    location_lng = models.FloatField()
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.biker.full_name} - {'Available' if self.is_available else 'Unavailable'}"

 # assuming Biker model is in the same app

class Earnings(models.Model):
    biker = models.OneToOneField(Biker, on_delete=models.CASCADE, related_name='earnings')
    daily_earning = models.FloatField(default=0)
    weekly_earning = models.FloatField(default=0)
    monthly_earning = models.FloatField(default=0)
    total_rides = models.PositiveIntegerField(default=0)
    acceptance_rate = models.FloatField(default=0)
    rating = models.FloatField(default=0)

    def __str__(self):
        return f"Earnings for {self.biker.full_name}"

