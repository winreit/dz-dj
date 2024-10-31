# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from rest_framework import generics, status

from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Measurement, Sensor
from .serializers import MeasurementSerializer, SensorSerializer





class MeasurementViewSet(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer



class SensorView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorChangeView(UpdateAPIView):
    queryset = Sensor.objects.all()
    Serializer = SensorSerializer


class SensorListCreateView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer