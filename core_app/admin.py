from django.contrib import admin
from .models import Ride,RideRequest,Transaction,Rating,History,price_info

@admin.register(Ride)
class RideAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'biker', 'pickup_location', 'dropoff_location', 'status', 'date', 'amount', 'payment_method')
    list_filter = ('status', 'payment_method', 'date')
    search_fields = ('user__username', 'biker__full_name', 'pickup_location', 'dropoff_location')

@admin.register(RideRequest)
class RideRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'biker', 'status')
    list_filter = ('status',)
    search_fields = ('user__username', 'biker__full_name')

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('transaction_id', 'ride', 'amount', 'payment_method', 'status', 'created_at')
    list_filter = ('payment_method', 'status', 'created_at')
    search_fields = ('transaction_id', 'ride__id')

@admin.register(Rating)
class RatingaAdmin(admin.ModelAdmin):
    list_display = ('ride','user','biker','rating','feedback_text','created_at')
    list_filter = ('ride','user','biker','created_at')
    search_fields = ('created_at','ride')

@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'ride', 'status', 'date', 'pickup', 'dropoff', 'amount')
    search_fields = ('rideId', 'user__username', 'pickup', 'dropoff')
    list_filter = ('status', 'date')
admin.site.register(price_info)    