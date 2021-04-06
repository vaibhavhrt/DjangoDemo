from rest_framework import viewsets

from .models import PaginationDemo, Incident, DateRangeAndDuration
from .serializers import PaginationDemoSerializer, IncidentSerializer, DateRangeAndDurationSerializer


class PaginationDemoViewSet(viewsets.ModelViewSet):
    serializer_class = PaginationDemoSerializer
    queryset = PaginationDemo.objects.all()


class IncidentViewSet(viewsets.ModelViewSet):
    serializer_class = IncidentSerializer
    queryset = Incident.objects.all()


class DateRangeAndDurationViewSet(viewsets.ModelViewSet):
    serializer_class = DateRangeAndDurationSerializer
    queryset = DateRangeAndDuration.objects.all()
