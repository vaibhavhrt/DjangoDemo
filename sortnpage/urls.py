from django.urls import path
from rest_framework import routers

from . import views
from .viewsets import PaginationDemoViewSet

router = routers.SimpleRouter()
router.register(r'pagination-demos', PaginationDemoViewSet)

urlpatterns = [
    path('pagination-demos/', views.PaginationDemoList.as_view(), name='PaginationDemoList'),
    path('pagination-demos-datatables/', views.PaginationDemoListDatatables.as_view(), name='PaginationDemoListDatatables'),
    path('pagination-demos-data/', views.PaginationDemoListData.as_view(), name='PaginationDemoListData'),
    path('pagination-demo/<pk>', views.PaginationDemoDetail.as_view(), name='PaginationDemoDetail'),
]
