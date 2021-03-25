from functools import reduce
from operator import and_

from django.views.generic import ListView, DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.core.paginator import Paginator
from django.http.response import JsonResponse
from django.db.models import Q

from .models import PaginationDemo
from .serializers import PaginationDemoSerializer
from .filters import PaginationDemoFilter


class PaginationDemoList(LoginRequiredMixin, ListView):
    model = PaginationDemo
    # login_url = '/api-auth/login/'
    paginate_by = 10
    # ordering = ['name']

    def get_ordering(self):
        ordering = self.request.GET.get("ordering", "amount")

        # validate ordering
        if ordering not in (
            "name",
            "amount",
            "-name",
            "-amount",
        ):
            ordering = "amount"

        return ordering


class PaginationDemoDetail(LoginRequiredMixin, DetailView):
    model = PaginationDemo
    # login_url = '/api-auth/login/'

    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg)
        obj = PaginationDemo.objects.get(uuId=pk)
        return obj


class PaginationDemoListDatatables(View):
    def get(self, request):
        return render(request, "sortnpage/paginationdemo_list_datatables.html")


class PaginationDemoListData(View):
    def get(self, request):
        # print(request.GET)

        # Pagination limit and offset
        try:
            start = int(request.GET.get("start", 0))
        except ValueError:
            start = 0
        try:
            length = int(request.GET.get("length", 10))
        except ValueError:
            length = 10

        columns = ["id", "name", "amount"]
        ordering = "name"

        # Order Column
        try:
            order_col = int(request.GET.get("order[0][column]", 1))
        except ValueError:
            order_col = 1
        if order_col:
            try:
                ordering = columns[order_col]
            except KeyError:
                pass

        # Order Direction
        order_dir = request.GET.get("order[0][dir]")
        if order_dir and order_dir == "desc":
            ordering = "-" + ordering

        allObjects = PaginationDemo.objects.all().order_by(ordering)
        filtered_objects = PaginationDemoFilter(request.GET, queryset=allObjects).qs

        # Add paginator
        # paginator = Paginator(allObjects, length)
        paginator = Paginator(filtered_objects, length)
        page = (start // length) + 1
        pageObjects_list = paginator.get_page(page)

        return JsonResponse(
            {
                "recordsTotal": paginator.count,
                "recordsFiltered": paginator.count,
                "data": PaginationDemoSerializer(pageObjects_list, many=True).data,
            }
        )
