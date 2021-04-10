import uuid
from django.db import models


class UserCreditCard(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    credit_card = models.ForeignKey(
        'payments.CreditCard',
        related_name='credit_card',
        on_delete=models.PROTECT,
        null=False,
        blank=False,
    )
    user = models.ForeignKey(
        'payments.User',
        related_name='user',
        on_delete=models.PROTECT,
        null=False,
        blank=False,
    )
    created_date = models.DateTimeField(auto_now=True)
