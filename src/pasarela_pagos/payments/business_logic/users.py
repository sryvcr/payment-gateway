import uuid
from pasarela_pagos.payments.helpers.email_checker import email_check
from pasarela_pagos.payments.models import (
    User,
    CreditCard,
    UserCreditCard,
    PaymentToken,
)


def get_user_by_id(id: str) -> User:
    try:
        user = User.objects.get(pk=id)
        return user
    except Exception as e:
        raise e


def get_credit_cards_by_user_id(id: str) -> User:
    try:
        users_credit_cards = UserCreditCard.objects.filter(user_id=id).all()
        credit_cards_id = [str(user_credit_card.credit_card_id) for user_credit_card in users_credit_cards]
        credit_cards = CreditCard.objects.filter(
            id__in=credit_cards_id
        )
        return credit_cards
    except Exception as e:
        raise e


def create_user(fullname: str, email: str) -> User:
    try:
        if not email_check(email):
            raise Exception('email not valid')
        if User.objects.filter(email=email).first():
            raise Exception('email already is in use')
        user = User(
            fullname=fullname,
            email=email,
        )
        user.save()
        return user
    except Exception as e:
        raise e


def link_credit_card(credit_card_id: str, user_id: str):
    try:
        link_exists = UserCreditCard.objects.filter(credit_card_id=credit_card_id).first()
        if link_exists:
            raise Exception('credit card already is in use')
        user_credit_card = UserCreditCard(
            user_id=user_id,
            credit_card_id=credit_card_id
        )
        user_credit_card.save()
        return user_credit_card
    except Exception as e:
        raise e


def update_user(id: str, update_info: dict) -> bool:
    try:
        user = User.objects.filter(id=id).first()
        if 'fullname' in update_info:
            user.fullname = update_info['fullname']
        if 'email' in update_info:
            if User.objects.filter(email=update_info['email']).first():
                raise Exception('email already is in use')
            user.email = update_info['email']
        user.save()
        return user
    except Exception as e:
        raise e


def create_payment_token(user_credit_card_id: str):
    try:
        link_exists = UserCreditCard.objects.filter(id=user_credit_card_id).first()
        if not link_exists:
            raise Exception('user credit card does not exist')
        unique_token = uuid.uuid3(uuid.NAMESPACE_DNS, user_credit_card_id)
        payment_token = PaymentToken(
            token=unique_token,
            used=False,
        )
        payment_token.save()
        return payment_token
    except Exception as e:
        raise e


def delete_user(user: User) -> bool:
    try:
        user.delete()
        return True
    except Exception as e:
        raise e
