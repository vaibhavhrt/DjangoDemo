from rest_framework import viewsets, response, status

from .models import PaginationDemo
from .serializers import PaginationDemoSerializer


class PaginationDemoViewSet(viewsets.ModelViewSet):
    serializer_class = PaginationDemoSerializer
    queryset = PaginationDemo.objects.all()
