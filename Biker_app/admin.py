
from django.contrib import admin
from .models import Biker, BikerAvailability,Earnings

@admin.register(Biker)
class BikerAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'cnic', 'phone_number', 'bike_model', 'vehicle_number', 'joined_at')
    search_fields = ('full_name', 'cnic', 'phone_number')
    list_filter = ('joined_at',)

@admin.register(BikerAvailability)
class BikerAvailabilityAdmin(admin.ModelAdmin):
    list_display = ('id', 'biker', 'is_available', 'location_lat', 'location_lng', 'updated_at')
    list_filter = ('is_available',)
    search_fields = ('biker__full_name', 'biker__cnic')

@admin.register(Earnings)
class EarningsAdmin(admin.ModelAdmin):
    list_display = ('biker', 'daily_earning', 'weekly_earning', 'monthly_earning', 'total_rides', 'acceptance_rate', 'rating')
    search_fields = ('biker__full_name', 'biker__cnic')

# Register your models here.
