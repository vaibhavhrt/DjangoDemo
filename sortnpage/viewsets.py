from rest_framework import viewsets

from .models import PaginationDemo, Incident
from .serializers import PaginationDemoSerializer, IncidentSerializer


class PaginationDemoViewSet(viewsets.ModelViewSet):
    serializer_class = PaginationDemoSerializer
    queryset = PaginationDemo.objects.all()


class IncidentViewSet(viewsets.ModelViewSet):
    serializer_class = IncidentSerializer
    queryset = Incident.objects.all()
