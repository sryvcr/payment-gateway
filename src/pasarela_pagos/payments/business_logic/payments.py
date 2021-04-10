from django.db import transaction
from pasarela_pagos.payments.models import (
    Payment,
    PaymentToken
)


def get_payment_by_id(id: str) -> Payment:
    try:
        payment = Payment.objects.get(pk=id)
        return payment
    except Exception as e:
        raise e


@transaction.atomic()
def create_payment(
    value_after_iva: int,
    value_total: int,
    iva: int,
    user_id: str,
    payment_token: str,
    dues: int,
    payment_reference: str,
    webhook_url: str
) -> Payment:
    try:
        token = validate_payment_token(payment_token)
        payment = Payment(
            value_after_iva=value_after_iva,
            value_total=value_total,
            iva=iva,
            user_id=user_id,
            payment_token=payment_token,
            dues=dues,
            payment_reference=payment_reference,
            webhook_url=webhook_url,
        )
        payment.save()
        token.used = True
        token.save()
        return payment
    except Exception as e:
        raise e


def validate_payment_token(payment_token: str) -> PaymentToken:
    try:
        token = PaymentToken.objects.filter(token=payment_token).first()
        if not token:
            raise Exception('payment token does not exist')
        if token.used:
            raise Exception('payment token not valid')
        return token
    except Exception as e:
        raise e
