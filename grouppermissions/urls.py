from django.urls import path
from rest_framework import routers

from . import views
from .viewsets import AccessLevelPermissionViewSet

router = routers.SimpleRouter()
router.register(r'access-level-permissions', AccessLevelPermissionViewSet)

urlpatterns = [
    path('access-level-permissions/', views.AccessLevelPermissionList.as_view(), name='AccessLevelPermissionList'),
]
