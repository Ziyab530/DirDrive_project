from django.shortcuts import render
from rest_framework import viewsets
from .models import Ride,RideRequest,Transaction,Rating,History,price_info
from .serializers import RideSerializer,RideRequestSerializer,TransactionSerializer,RatingSerializer,HistorySerializer,price_infoSerializer
from rest_framework.permissions import IsAuthenticated
from .filters import (
    RideFilter, RideRequestFilter, TransactionFilter,
    RatingFilter, HistoryFilter,price_infoFilter
)
from django_filters.rest_framework import DjangoFilterBackend

class RideViewSet(viewsets.ModelViewSet):
    queryset = Ride.objects.all()
    serializer_class = RideSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = RideFilter

class RideRequestViewSet(viewsets.ModelViewSet):
    queryset = RideRequest.objects.all()
    serializer_class = RideRequestSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = RideRequestFilter

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TransactionFilter

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = RatingFilter

class HistoryViewSet(viewsets.ModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = HistoryFilter

    def get_queryset(self):
        # Only show history for the logged-in user
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
class price_infoViewSet(viewsets.ModelViewSet):
    queryset = price_info.objects.all()
    serializer_class = price_infoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = price_infoFilter
