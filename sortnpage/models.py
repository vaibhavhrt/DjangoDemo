from django.db import models
import uuid


# Create your models here.
class PaginationDemo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=127, null=False)
    amount = models.PositiveIntegerField(null=False)
    uuId = models.UUIDField(default=uuid.uuid4, editable=False, db_index=True)
