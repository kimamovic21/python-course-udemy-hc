def multiplication_table(number: int) -> list[str]:
    table = []

    for multiplier in range(1, 11):
        table.append(f"{number} x {multiplier} = {number * multiplier}")

    return table
