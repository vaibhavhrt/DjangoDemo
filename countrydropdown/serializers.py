from rest_framework import serializers

from .models import CountrySelect, Location


class CountrySelectSerializer(serializers.ModelSerializer):

    class Meta:
        model = CountrySelect
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = '__all__'
