loyalty_points = 0


def process_transactions(transactions: list[int]) -> int:
    global loyalty_points
    total = sum(transactions)

    def apply_bonus():
        nonlocal total
        if total > 1000:
            total += 50

    apply_bonus()
    loyalty_points += total // 100
    return total
