from django.conf.urls import url
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView

from .models import PhoneNumbers


# Create your views here.
class PhoneNumbersList(ListView):
    model = PhoneNumbers


class PhoneNumbersCreate(CreateView):
    model = PhoneNumbers
    fields = "__all__"
    success_url = "/phonenumbers/list"
    # success_url = "/phonenumbers/create"


class PhoneNumbersUpdate(UpdateView):
    model = PhoneNumbers
    fields = "__all__"
    success_url = "/phonenumbers/list"
