from django.db import models
from django.utils import timezone
from django.conf import settings
from Biker_app.models import Biker
from users_app.models import User
import googlemaps


class Ride(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    )

    PAYMENT_METHOD_CHOICES = (
        ('cash', 'Cash'),
        ('jazzcash', 'JazzCash'),
        ('easypaisa', 'EasyPaisa'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rides')
    biker = models.ForeignKey(Biker, on_delete=models.CASCADE, related_name='rides')
    pickup_location = models.CharField(max_length=255)
    dropoff_location = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    date = models.DateTimeField(default=timezone.now)
    amount = models.FloatField()
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)

    def __str__(self):
        return f"Request from {self.user.username} to {self.biker.full_name} - {self.status}"
    
   



class RideRequest(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
        ('cancelled', 'Cancelled'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ride_requests')
    biker = models.ForeignKey(Biker, on_delete=models.CASCADE, related_name='ride_requests')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Request from {self.user.username} to {self.biker.full_name} - {self.status}"
 

class Transaction(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    )

    PAYMENT_METHOD_CHOICES = (
        ('cash', 'Cash'),
        ('jazzcash', 'JazzCash'),
        ('easypaisa', 'EasyPaisa'),
    )

    ride = models.ForeignKey(Ride, on_delete=models.CASCADE, related_name='transactions')
    amount = models.FloatField()
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    transaction_id = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Transaction {self.transaction_id} ({self.status})"

class Rating(models.Model):
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings_given')
    biker = models.ForeignKey(Biker, on_delete=models.CASCADE, related_name='ratings_received')
    rating = models.FloatField()
    feedback_text = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Rating {self.rating} by {self.user.username} for {self.biker.full_name}"



class History(models.Model):
    STATUS_CHOICES = [
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
        ('ongoing', 'Ongoing'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ride_history')
    ride = models.ForeignKey(Ride,on_delete=models.CASCADE,related_name='ride_id') 
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    date = models.DateTimeField()
    pickup = models.CharField(max_length=255)
    dropoff = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"History for Ride {self.rideId} by {self.user.username}"

class price_info(models.Model):
    price_id = models.CharField(max_length=100)
    pickup_location = models.CharField(max_length=250)
    dropoff_location = models.CharField(max_length=250)
    price = models.CharField(max_length=250)
    def __str__(self):
        return f"price info for Ride {self.peice_id} by {self.user.username}"
    

    


