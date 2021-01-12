from django.urls import path
from rest_framework import routers

from . import views
from .viewsets import ParentViewSet

router = routers.SimpleRouter()
router.register(r'parents', ParentViewSet)

urlpatterns = [
    path('<parent_id>/parent-detail', views.ParentDetailView.as_view(), name='ParentDetailView'),
    path('<parent_id>/create-childA', views.ChildACreateView.as_view(), name='ChildACreateView'),
]
