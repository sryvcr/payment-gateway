from pasarela_pagos.payments.models import CreditCard
from pasarela_pagos.payments.helpers.luhn_checker import is_luhn_valid
from pasarela_pagos.payments.helpers.franchise_checker import franchise_checker


def create_credit_card(card_number: int, due_date: str) -> CreditCard:
    try:
        if not is_luhn_valid(card_number):
            raise Exception('credit card number not valid')
        franchise = franchise_checker(card_number)
        if not franchise:
            raise Exception('credit card franchise not valid')
        credit_card = CreditCard(
            card_number=card_number,
            franchise=franchise,
            due_date=due_date,
        )
        credit_card.save()
        return credit_card
    except Exception as e:
        raise e