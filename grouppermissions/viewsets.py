from rest_framework import viewsets, response, status

from .models import AccessLevelPermission
from .serializers import AccessLevelPermissionSerializer


class AccessLevelPermissionViewSet(viewsets.ModelViewSet):
    serializer_class = AccessLevelPermissionSerializer
    queryset = AccessLevelPermission.objects.all()
