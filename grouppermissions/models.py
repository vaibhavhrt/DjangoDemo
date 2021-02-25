from django.db import models
from django.contrib.auth import get_user_model


class AccessLevelPermission(models.Model):
    name = models.CharField(max_length=127)
    access_level = models.PositiveIntegerField(
        choices=((1, "One"), (2, "Two"), (3, "Three"))
    )


class CreatorPermission(models.Model):
    name = models.CharField(max_length=127)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
