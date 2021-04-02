from django.db import models

# Create your models here.
class Location(models.Model):
    city = models.CharField(max_length=127)
    state = models.CharField(max_length=127)
    country = models.CharField(max_length=127)

    def __str__(self) -> str:
        return f"{self.city}, {self.state}, {self.country}"


class CountrySelect(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    name = models.CharField(max_length=127)

    def __str__(self) -> str:
        return self.name + self.location.city
