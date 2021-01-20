from rest_framework import viewsets, response, status

from .models import Parent
from .serializers import ParentSerializer


class ParentViewSet(viewsets.ModelViewSet):
    serializer_class = ParentSerializer
    queryset = Parent.objects.all()

    # def list():
    #     pass

    # def create(self, request, *args, **kwargs):
    #     return response.Response({'msg': 'Custom Response'}, status=status.HTTP_400_BAD_REQUEST)
