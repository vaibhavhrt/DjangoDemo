from rest_framework import viewsets, permissions

from .models import AccessLevelPermission, CreatorPermission
from .serializers import AccessLevelPermissionSerializer, CreatorPermissionSerializer


class AccessLevelPermissionViewSet(viewsets.ModelViewSet):
    serializer_class = AccessLevelPermissionSerializer
    queryset = AccessLevelPermission.objects.all()


class CreatorPermissionViewSet(viewsets.ModelViewSet):
    serializer_class = CreatorPermissionSerializer
    queryset = CreatorPermission.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
