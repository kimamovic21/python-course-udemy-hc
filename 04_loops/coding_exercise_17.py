def simulate_atm_withdrawals(balance: int, withdrawals: list[int]) -> list[str]:
    messages = []
    index = 0

    while index < len(withdrawals):
        amount = withdrawals[index]

        if balance >= amount:
            balance -= amount
            messages.append(f"Withdrawn: {amount}")
        else:
            messages.append(f"Insufficient funds for requested amount: {amount}")

        index += 1

    messages.append(f"Remaining Balance: {balance}")
    return messages
