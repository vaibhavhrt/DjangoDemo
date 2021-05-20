from django.db import models

# Create your models here.
class Todo(models.Model):
    name = models.CharField(max_length=127)
    status = models.PositiveIntegerField(choices=((0, 'pending', ), (1, 'completed', ), ))
