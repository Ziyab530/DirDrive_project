from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RideViewSet,RideRequestViewSet,TransactionViewSet,RatingViewSet,HistoryViewSet,price_infoViewSet

router = DefaultRouter()
router.register(r'rides', RideViewSet)
router.register(r'ride-requests', RideRequestViewSet)
router.register(r'transactions', TransactionViewSet)
router.register(r'ratings', RatingViewSet)
router.register(r'history', HistoryViewSet, basename='history')
router.register(r'price_info',price_infoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
