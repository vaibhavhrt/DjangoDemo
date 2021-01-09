from rest_framework import viewsets

from .models import Parent
from .serializers import ParentSerializer


class ParentViewSet(viewsets.ModelViewSet):
    serializer_class = ParentSerializer
    queryset = Parent.objects.all()
