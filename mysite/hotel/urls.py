from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('properties', PropertyViewSet)
router.register('images', ImageViewSet)
router.register('bookings', BookingViewSet)
router.register('reviews', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('property/<int:pk>/', PropertyDetailAPIView.as_view(), name='property_detail')

]
