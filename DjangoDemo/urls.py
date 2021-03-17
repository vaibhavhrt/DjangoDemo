"""DjangoDemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from user.urls import router as user_router
from nestedrelations.urls import router as nestedrelations_router
from sortnpage.urls import router as sortnpage_router
from grouppermissions.urls import router as grouppermissions_router
from countrydropdown.urls import router as countrydropdown_router

router = routers.DefaultRouter()
router.registry.extend(user_router.registry)
router.registry.extend(nestedrelations_router.registry)
router.registry.extend(sortnpage_router.registry)
router.registry.extend(grouppermissions_router.registry)
router.registry.extend(countrydropdown_router.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('nestedrelations/',include('nestedrelations.urls')),
    path('sortnpage/',include('sortnpage.urls')),
    path('grouppermissions/',include('grouppermissions.urls')),
    path('countrydropdown/',include('countrydropdown.urls')),
]
