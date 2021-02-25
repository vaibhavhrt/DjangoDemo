from rest_framework import serializers

from .models import AccessLevelPermission, CreatorPermission


class AccessLevelPermissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = AccessLevelPermission
        fields = '__all__'
from .models import AccessLevelPermission, CreatorPermission


class CreatorPermissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = CreatorPermission
        fields = '__all__'
        read_only_fields = ('created_by', )
