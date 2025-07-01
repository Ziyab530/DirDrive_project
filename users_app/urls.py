from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserRegisterView, UserLoginView, UserLogoutView, UserProfileViewSet, BikerApplicationViewSet,SupportIssueViewSet

router = DefaultRouter()
router.register('profiles', UserProfileViewSet, basename='userprofile')
router.register('biker-applications', BikerApplicationViewSet, basename='bikerapplication')
router.register('support-issues', SupportIssueViewSet, basename='supportissue')

urlpatterns = [
    path('', include(router.urls)),
    path('register', UserRegisterView.as_view(), name='register'),
    path('login', UserLoginView.as_view(), name='login'),
    path('logout', UserLogoutView.as_view(), name='logout'),
]
