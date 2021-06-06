from django.urls import path
from rest_framework import routers

from .viewsets import PhoneNumbersViewSet
from . import views

router = routers.SimpleRouter()
router.register(r'phone-numbers', PhoneNumbersViewSet)

urlpatterns = [
    path('list', views.PhoneNumbersList.as_view(), name="PhoneNumbersList"),
    path('create', views.PhoneNumbersCreate.as_view(), name="PhoneNumbersCreate"),
]
