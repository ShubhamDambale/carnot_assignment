from django.db import models

# Create your models here.


class Device(models.Model):
    deviceId = models.CharField(max_length=100, unique=True)


class DeviceData(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    latitude = models.FloatField()
    longitude = models.FloatField()
