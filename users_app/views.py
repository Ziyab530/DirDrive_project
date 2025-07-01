from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.contrib.auth import authenticate, login, logout
from .models import User
from rest_framework import viewsets
from .serializers import UserRegisterSerializer
from .models import UserProfile
from .serializers import UserProfileSerializer
from rest_framework import viewsets, permissions
from .models import BikerApplication,SupportIssue
from .serializers import BikerApplicationSerializer,SupportIssueSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import UserProfileFilter, BikerApplicationFilter, SupportIssueFilter


class UserRegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return Response({"message": "Login successful."}, status=status.HTTP_200_OK)
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


class UserLogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({"message": "Logout successful."}, status=status.HTTP_200_OK)



class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserProfileFilter
    


class BikerApplicationViewSet(viewsets.ModelViewSet):
    queryset = BikerApplication.objects.all()
    serializer_class = BikerApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = BikerApplicationFilter

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class SupportIssueViewSet(viewsets.ModelViewSet):
    queryset = SupportIssue.objects.all()
    serializer_class = SupportIssueSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = SupportIssueFilter

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


