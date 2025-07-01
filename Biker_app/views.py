from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Biker,BikerAvailability,Earnings
from .serializers import BikerLoginSerializer, BikerSerializer,BikerAvailabilitySerializer,EarningsSerializer
from .filters import BikerFilter, BikerAvailabilityFilter, EarningsFilter
from django_filters.rest_framework import DjangoFilterBackend

class BikerLoginView(APIView):
    def post(self, request):
        serializer = BikerLoginSerializer(data=request.data)
        if serializer.is_valid():
            cnic = serializer.validated_data['cnic']
            password = serializer.validated_data['password']
            try:
                biker = Biker.objects.get(cnic=cnic)
                if biker.password == password:
                    return Response({
                        "message": "Login successful",
                        "biker": BikerSerializer(biker).data
                    }, status=status.HTTP_200_OK)
                else:
                    return Response({"error": "Invalid password"}, status=status.HTTP_401_UNAUTHORIZED)
            except Biker.DoesNotExist:
                return Response({"error": "Biker not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BikerViewSet(viewsets.ModelViewSet):
    queryset = Biker.objects.all()
    serializer_class = BikerSerializer
    permission_classes = [IsAuthenticated] 
    filter_backends = [DjangoFilterBackend]  # Change to IsAuthenticated for protection
    filterset_class = BikerFilter



class BikerAvailabilityViewSet(viewsets.ModelViewSet):
    queryset = BikerAvailability.objects.all()
    serializer_class = BikerAvailabilitySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BikerAvailabilityFilter


class EarningsViewSet(viewsets.ModelViewSet):
    queryset = Earnings.objects.all()
    serializer_class = EarningsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = EarningsFilter
