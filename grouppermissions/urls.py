from django.urls import path
from rest_framework import routers

from . import views
from .viewsets import AccessLevelPermissionViewSet, CreatorPermissionViewSet

router = routers.SimpleRouter()
router.register(r'access-level-permissions', AccessLevelPermissionViewSet)
router.register(r'creator-permissions', CreatorPermissionViewSet)

urlpatterns = [
    path('access-level-permissions/', views.AccessLevelPermissionList.as_view(), name='AccessLevelPermissionList'),
    path('creator-permissions/', views.CreatorPermissionList.as_view(), name='CreatorPermissionList'),
]
