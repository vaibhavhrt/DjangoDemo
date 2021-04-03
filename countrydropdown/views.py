from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView
from django.http.response import JsonResponse
from django.core.paginator import Paginator

from .models import Location, CountrySelect
from .serializers import LocationSerializer, CountrySelectDatatablesSerializer
from .forms import CountrySelectCreateForm


# Create your views here.
class DropDownOptions(View):
    def get(self, request):
        country = request.GET.get("country", None)
        state = request.GET.get("state", None)
        country_list = []
        state_list = []
        city_list = []
        if state:
            city_q = Location.objects.filter(state=state)
            city_list = LocationSerializer(city_q, many=True).data
        elif country:
            # state_q = Location.objects.filter(country=country).distinct('state').values_list('state', flat=True)
            # state_list = tuple(state_q)
            state_q = Location.objects.filter(country=country).values_list(
                "state", flat=True
            )
            state_list = tuple(set(state_q))
        else:
            # country_q = tuple(Location.objects.distinct('country').values_list('country', flat=True))
            # country_list = tuple(country_q)
            country_q = Location.objects.values_list("country", flat=True)
            country_list = tuple(set(country_q))
        return JsonResponse(
            {
                "country": country_list,
                "state": state_list,
                "city": city_list,
            }
        )


class CountrySelectCreate(View):
    def get(self, request):
        form = CountrySelectCreateForm()
        country_q = Location.objects.values_list("country", flat=True)
        country_list = tuple(set(country_q))
        context = {"form": form, "country_list": country_list}
        return render(request, "countrydropdown/CountrySelectCreate.html", context)

    def post(self, request):
        post_data = request.POST.copy()
        form = CountrySelectCreateForm(post_data)
        if form.is_valid():
            form.save()
            return redirect(reverse('CountrySelectList'))
        country_q = Location.objects.values_list("country", flat=True)
        country_list = tuple(set(country_q))
        context = {"form": form, "country_list": country_list}
        return render(request, "countrydropdown/CountrySelectCreate.html", context)


class CountrySelectList(View):
    def get(self, request):
        return render(request, "countrydropdown/CountrySelectList.html")


class CountrySelectDatatables(View):
    def get(self, request):
        # Pagination limit and offset
        try:
            start = int(request.GET.get("start", 0))
        except ValueError:
            start = 0
        try:
            length = int(request.GET.get("length", 10))
        except ValueError:
            length = 10

        columns = ["id", "name", "amount", "createdAt"]
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

        allObjects = CountrySelect.objects.all().order_by(ordering)
        # filtered_objects = PaginationDemoFilter(request.GET, queryset=allObjects).qs

        # Add paginator
        paginator = Paginator(allObjects, length)
        # paginator = Paginator(filtered_objects, length)
        page = (start // length) + 1
        pageObjects_list = paginator.get_page(page)

        return JsonResponse(
            {
                # "recordsTotal": paginator.count,
                "recordsTotal": allObjects.count(),
                "recordsFiltered": paginator.count,
                "data": CountrySelectDatatablesSerializer(pageObjects_list, many=True).data,
            }
        )


class CountrySelectDetail(DetailView):
    model = CountrySelect


class LocationDetail(DetailView):
    model = Location
