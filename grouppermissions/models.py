from django.db import models

# Create your models here.
class AccessLevelPermission(models.Model):
    name = models.CharField(max_length=127)
    access_level = models.PositiveIntegerField(
        choices=((1, "One"), (2, "Two"), (3, "Three"))
    )
