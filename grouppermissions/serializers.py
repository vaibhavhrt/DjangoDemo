from rest_framework import serializers

from .models import AccessLevelPermission


class AccessLevelPermissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = AccessLevelPermission
        fields = '__all__'
