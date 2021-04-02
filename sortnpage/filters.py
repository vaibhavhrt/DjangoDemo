import django_filters

from .models import PaginationDemo


class PaginationDemoFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")
    createdAt_lte = django_filters.DateFilter(field_name="createdAt", lookup_expr="lte")
    createdAt_gte = django_filters.DateFilter(field_name="createdAt", lookup_expr="gte")

    class Meta:
        model = PaginationDemo
        # fields = ["amount"]
        fields = "__all__"
