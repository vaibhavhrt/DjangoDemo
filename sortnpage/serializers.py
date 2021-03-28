from rest_framework import serializers

from .models import PaginationDemo, Incident


class PaginationDemoSerializer(serializers.ModelSerializer):

    class Meta:
        model = PaginationDemo
        fields = '__all__'


class IncidentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Incident
        fields = '__all__'
