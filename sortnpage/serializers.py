from rest_framework import serializers

from .models import PaginationDemo, Incident, DateRangeAndDuration


class PaginationDemoSerializer(serializers.ModelSerializer):

    class Meta:
        model = PaginationDemo
        fields = '__all__'


class IncidentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Incident
        fields = '__all__'


class DateRangeAndDurationSerializer(serializers.ModelSerializer):

    class Meta:
        model = DateRangeAndDuration
        fields = '__all__'
