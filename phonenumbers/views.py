from django.shortcuts import render
from django.views.generic import ListView

from .models import PhoneNumbers


# Create your views here.
class PhoneNumbersList(ListView):
    model = PhoneNumbers
