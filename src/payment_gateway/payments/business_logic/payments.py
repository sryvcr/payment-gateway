from typing import List, Union
from django.db import transaction
from payment_gateway.payments.models import (
    Payment,
    PaymentToken,
    Repayment
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


@transaction.atomic()
def create_repayment(payment_id: str, reason: str, value: int) -> List[Union[Payment, Repayment]]:
    try:
        repayment_value_total = 0
        payment = Payment.objects.filter(id=payment_id).first()
        if not payment:
            raise Exception('payment does not exist')
        if value > payment.value_total:
            raise Exception('current repayment value exceeds the payment value')
        repayments = Repayment.objects.filter(payment_id=payment_id).all()
        if repayments:
            for repayment in repayments:
                repayment_value_total += repayment.value
        if repayment_value_total + value > payment.value_total:
            raise Exception('current repayment value with previous repayments exceeds the payment value')
        repayment = Repayment(
            payment_id=payment_id,
            reason=reason,
            value=value
        )
        repayment.save()
        if payment.status != payment.REVERSED:
            payment.status = payment.REVERSED
            payment.save()
        return payment
    except Exception as e:
        raise e


def validate_payment_token(payment_token: str) -> PaymentToken:
    try:
        token = PaymentToken.objects.filter(
            token=payment_token,
            used=False
        ).first()
        if not token:
            raise Exception('payment token does not exist')
        if token.used:
            raise Exception('payment token not valid')
        return token
    except Exception as e:
        raise e
