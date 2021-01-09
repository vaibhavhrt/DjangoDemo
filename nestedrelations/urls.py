from rest_framework import routers

from .viewsets import ParentViewSet

router = routers.SimpleRouter()
router.register(r'parents', ParentViewSet)
