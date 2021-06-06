from rest_framework import viewsets

from .models import PhoneNumbers
from .serializers import PhoneNumbersSerializer


class PhoneNumbersViewSet(viewsets.ModelViewSet):
    serializer_class = PhoneNumbersSerializer
    queryset = PhoneNumbers.objects.all()
