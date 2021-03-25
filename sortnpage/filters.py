import django_filters

from .models import PaginationDemo


class PaginationDemoFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = PaginationDemo
        fields = ["amount"]
