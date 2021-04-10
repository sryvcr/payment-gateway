from pasarela_pagos.payments.helpers.email_checker import email_check
from pasarela_pagos.payments.models import User


def get_user_by_id(id: str) -> User:
    try:
        user = User.objects.get(pk=id)
        return user
    except Exception as e:
        raise e


def create_user(fullname: str, email: str) -> User:
    try:
        if not email_check(email):
            raise Exception('email not valid')
        if User.objects.filter(email=email).first():
            raise Exception('email already in use')
        user = User(
            fullname=fullname,
            email=email,
        )
        user.save()
        return user
    except Exception as e:
        raise e
