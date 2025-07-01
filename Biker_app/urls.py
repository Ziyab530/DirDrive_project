from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BikerLoginView, BikerViewSet,BikerAvailabilityViewSet, EarningsViewSet

router = DefaultRouter()
router.register(r'bikers', BikerViewSet, basename='biker')
router.register(r'biker-availability', BikerAvailabilityViewSet, basename='availability')
router.register(r'earnings', EarningsViewSet, basename='earnings')

urlpatterns = [
    path('', include(router.urls)),
    path('Biker-login', BikerLoginView.as_view(), name='biker-login'),
]
