import re

def normalize_phone(phone_number: str) -> str:
    digits = re.sub(r"\D", "", phone_number)

    if digits == "":
        return ""

    if digits.startswith("380"):
        return "+" + digits
    else:
        return "+38" + digits
