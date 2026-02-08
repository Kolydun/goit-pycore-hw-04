import re

def normalize_phone(phone_number: str) -> str:
    cleaned = re.sub(r"[^\d+]", "", phone_number)

    if cleaned.startswith("+"):
        return cleaned

    if cleaned.startswith("380"):
        return "+" + cleaned

    return "+38" + cleaned
