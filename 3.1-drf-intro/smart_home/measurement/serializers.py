from rest_framework import serializers

from .models import Measurement, Sensor

# TODO: опишите необходимые сериализаторы





class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = 'name', 'description'


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = 'sensor_id', 'temperature', 'created_at'

