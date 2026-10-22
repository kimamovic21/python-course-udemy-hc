def check_loan_eligibility(age: int, income: float) -> str:
    if age >= 21:
        if income >= 25_000:
            return "Eligible for loan"
        else:
            return "Not eligible: Income too low"
    else:
        return "Not eligible: Age must be 21 or above"
