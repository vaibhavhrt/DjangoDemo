from django.db import models


# Create your models here.
class PhoneNumbers(models.Model):
    name = models.CharField(max_length=127)
    phone_numbers = models.TextField()
