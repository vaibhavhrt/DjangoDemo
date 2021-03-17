from django.shortcuts import render, redirect
from django.views import View
from django.http.response import JsonResponse

from .models import Location, CountrySelect
from .serializers import LocationSerializer
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
            return redirect("/country-selects/")
        country_q = Location.objects.values_list("country", flat=True)
        country_list = tuple(set(country_q))
        context = {"form": form, "country_list": country_list}
        return render(request, "countrydropdown/CountrySelectCreate.html", context)
