from rest_framework import serializers
from .models import Biker,BikerAvailability,Earnings

class BikerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Biker
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

class BikerLoginSerializer(serializers.Serializer):
    cnic = serializers.CharField()
    password = serializers.CharField()


class BikerAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = BikerAvailability
        fields = '__all__'

class EarningsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Earnings
        fields = '__all__'