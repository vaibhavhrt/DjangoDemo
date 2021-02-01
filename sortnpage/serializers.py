from rest_framework import serializers

from .models import PaginationDemo


class PaginationDemoSerializer(serializers.ModelSerializer):

    class Meta:
        model = PaginationDemo
        fields = '__all__'
