from django.db import models
import uuid


# Create your models here.
class PaginationDemo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=127, null=False)
    amount = models.PositiveIntegerField(null=False)
    uuId = models.UUIDField(default=uuid.uuid4, editable=False, db_index=True)
    createdAt = models.DateField(auto_now_add=True)


class Incident(models.Model):
    number = models.CharField(max_length=127, null=False)  # A123-00, A123-01
    iteration = models.PositiveIntegerField(null=False, editable=False)  # 0
    date = models.DateField()

    def save(self, *args, **kwargs):
        if self.pk is None:  # New object is being created
            self.iteration = int(self.number.split("-")[-1])
        super().save(*args, **kwargs)
