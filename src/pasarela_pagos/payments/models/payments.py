import uuid
from django.db import models


class Payment(models.Model):
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
    PENDING = "PENDING"
    REVERSED = "REVERSED"

    STATUS_CHOICES = (
        (APPROVED, APPROVED),
        (REJECTED, REJECTED),
        (PENDING, PENDING),
        (REVERSED, REVERSED)
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    value_after_iva = models.BigIntegerField()
    value_total = models.BigIntegerField()
    iva = models.BigIntegerField()
    status = models.CharField(max_length=25, choices=STATUS_CHOICES, default=PENDING)
    user = models.ForeignKey(
        'payments.User',
        on_delete=models.PROTECT,
        null=False,
        blank=False,
    )
    payment_token = models.CharField(max_length=40)
    dues = models.IntegerField()
    payment_reference = models.CharField(max_length=40)
    webhook_url = models.URLField()
    created_date = models.DateTimeField(auto_now_add=True)
