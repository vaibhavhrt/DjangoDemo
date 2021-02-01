from django.urls import path
from rest_framework import routers

from . import views
from .viewsets import PaginationDemoViewSet

router = routers.SimpleRouter()
router.register(r'pagination-demos', PaginationDemoViewSet)

urlpatterns = [
    path('pagination-demos/', views.PaginationDemoList.as_view(), name='PaginationDemoList'),
    path('pagination-demo/<pk>', views.PaginationDemoDetail.as_view(), name='PaginationDemoDetail'),
]
