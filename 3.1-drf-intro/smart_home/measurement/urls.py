from django.urls import path

from .serializers import MeasurementSerializer, SensorSerializer

urlpatterns = [
    path('sensors/', SensorSerializer.as_view()),
    path('measurements/', MeasurementSerializer.as_view()),

    # TODO: зарегистрируйте необходимые маршруты
]
