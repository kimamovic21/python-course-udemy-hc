def verify_age(age_str: str) -> str:
    age = int(age_str)
    return "Access Granted" if age >= 18 else "Access Denied"
