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


def update_user(id: str, update_info: dict) -> bool:
    try:
        user = User.objects.filter(id=id).first()
        if 'fullname' in update_info:
            user.fullname = update_info['fullname']
        if 'email' in update_info:
            if User.objects.filter(email=update_info['email']).first():
                raise Exception('email already in use')
            user.email = update_info['email']
        user.save()
        return user
    except Exception as e:
        raise e


def delete_user(user: User) -> bool:
    try:
        user.delete()
        return True
    except Exception as e:
        raise e
