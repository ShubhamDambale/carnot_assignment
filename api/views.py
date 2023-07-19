from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Device, DeviceData


def get_latest_device_info(request, deviceId):
    device = get_object_or_404(Device, deviceId=deviceId)
    latest_data = device.devicedata_set.latest('timestamp')
    response = {
        'deviceId': deviceId,
        'timestamp': latest_data.timestamp,
        'latitude': latest_data.latitude,
        'longitude': latest_data.longitude
    }
    return JsonResponse(response)


def get_device_location(request, deviceId):
    device = get_object_or_404(Device, deviceId=deviceId)
    data_points = device.devicedata_set.order_by('timestamp')
    start_location = data_points.first()
    end_location = data_points.last()
    response = {
        'startLocation': (start_location.latitude, start_location.longitude),
        'endLocation': (end_location.latitude, end_location.longitude)
    }
    return JsonResponse(response)


def get_device_locations(request, deviceId):
    start_time = request.GET.get('start')
    end_time = request.GET.get('end')
    device = get_object_or_404(Device, deviceId=deviceId)
    data_points = device.devicedata_set.filter(
        timestamp__range=(start_time, end_time)).order_by('timestamp')
    response = {
        'locations': [{
            'latitude': data.latitude,
            'longitude': data.longitude,
            'timestamp': data.timestamp
        } for data in data_points]
    }
    return JsonResponse(response)
