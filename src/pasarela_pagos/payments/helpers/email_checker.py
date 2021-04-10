import re


regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'


def email_check(email: str) -> bool:
    if(re.search(regex, email)):
        return True
    else:
        return False
