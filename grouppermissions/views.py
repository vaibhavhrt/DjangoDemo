# from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet

from .models import AccessLevelPermission, CreatorPermission


class AccessLevelPermissionList(LoginRequiredMixin, ListView):
    model = AccessLevelPermission

    def get_queryset(self) -> QuerySet:
        queryset = super().get_queryset()
        user = self.request.user
        if user.is_superuser:
            return queryset
        if user.is_staff:
            return queryset.filter(access_level__lte=2)
        return queryset.filter(access_level__lte=1)


class CreatorPermissionList(LoginRequiredMixin, ListView):
    model = CreatorPermission

    def get_queryset(self) -> QuerySet:
        queryset = super().get_queryset()
        user = self.request.user
        # if user.is_superuser:
        #     return queryset
        return queryset.filter(created_by=user)
