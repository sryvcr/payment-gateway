def franchise_checker(card_number: int) -> str:
    card_number = str(card_number)
    if int(card_number[0]) == 4 and len(card_number) in (13, 16):
        return "Visa"
    elif int(card_number[0]) == 5 and len(card_number) == 16:
        return "Mastercard"
    elif int(card_number[0]) == 3 and int(card_number[1]) in (4, 7) and len(card_number) == 15:
        return "American Express"
    else:
        return None
