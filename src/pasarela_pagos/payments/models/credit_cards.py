import uuid
from django.db import models


class CreditCard(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    card_number = models.BigIntegerField(unique=True)
    franchise = models.CharField(max_length=40)
    due_date = models.CharField(max_length=10)
    created_date = models.DateTimeField(auto_now=True)
