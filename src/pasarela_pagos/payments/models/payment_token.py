import uuid
from django.db import models


class PaymentToken(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    token = models.CharField(max_length=40)
    used = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
