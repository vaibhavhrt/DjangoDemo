from django.urls import path
from rest_framework import routers

from . import views
from .viewsets import PaginationDemoViewSet, IncidentViewSet, DateRangeAndDurationViewSet

router = routers.SimpleRouter()
router.register(r'pagination-demos', PaginationDemoViewSet)
router.register(r'incidents', IncidentViewSet)
router.register(r'date-range-and-durations', DateRangeAndDurationViewSet)

urlpatterns = [
    path('pagination-demos/', views.PaginationDemoList.as_view(), name='PaginationDemoList'),
    path('pagination-demos-datatables/', views.PaginationDemoListDatatables.as_view(), name='PaginationDemoListDatatables'),
    path('pagination-demos-data/', views.PaginationDemoListData.as_view(), name='PaginationDemoListData'),
    path('pagination-demo/<pk>', views.PaginationDemoDetail.as_view(), name='PaginationDemoDetail'),
    path('incident-create/', views.IncidentCreateView.as_view(), name='IncidentCreate'),
    path('date-range-and-durations-create/', views.DateRangeAndDurationCreateView.as_view(), name='DateRangeAndDurationCreate'),
]
