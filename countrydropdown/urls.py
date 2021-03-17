from django.urls import path
from rest_framework import routers

from . import views
from .viewsets import CountrySelectViewSet, LocationViewSet

router = routers.SimpleRouter()
router.register(r'country-selects', CountrySelectViewSet)
router.register(r'locations', LocationViewSet)

urlpatterns = [
    path('country-select-options/', views.DropDownOptions.as_view(), name='DropDownOptions'),
    path('country-select-create/', views.CountrySelectCreate.as_view(), name='CountrySelectCreate'),
]
