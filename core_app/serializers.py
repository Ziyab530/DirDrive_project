from rest_framework import serializers
from .models import Ride,RideRequest,Transaction,Rating,History,price_info

class RideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = '__all__'

class RideRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RideRequest
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'

class price_infoSerializer(serializers.ModelSerializer):
    class Meta:
        model = price_info
        fields = '__all__'
