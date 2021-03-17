from rest_framework import viewsets, response, status

from .models import CountrySelect, Location
from .serializers import CountrySelectSerializer, LocationSerializer


class CountrySelectViewSet(viewsets.ModelViewSet):
    serializer_class = CountrySelectSerializer
    queryset = CountrySelect.objects.all()


class LocationViewSet(viewsets.ModelViewSet):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()
