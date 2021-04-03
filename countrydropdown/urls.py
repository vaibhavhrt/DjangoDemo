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
    path('country-select-list/', views.CountrySelectList.as_view(), name='CountrySelectList'),
    path('country-select-datatables/', views.CountrySelectDatatables.as_view(), name='CountrySelectDatatables'),
    path('country-select/<int:pk>/', views.CountrySelectDetail.as_view(), name='CountrySelectDetail'),
    path('location/<int:pk>/', views.LocationDetail.as_view(), name='LocationDetail'),
]
