from django.urls import path
from .views import get_latest_device_info, get_device_location, get_device_locations

urlpatterns = [
    path('device/latest/<str:deviceId>/', get_latest_device_info),
    path('device/location/<str:deviceId>/', get_device_location),
    path('device/locations/<str:deviceId>/', get_device_locations),
]
