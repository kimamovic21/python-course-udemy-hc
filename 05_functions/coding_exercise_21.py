def generate_invoice(
    customer_name: str = "Guest", *items: str, **charges: float
) -> str:
    lines = [f"Invoice for {customer_name}:"]

    if items:
        lines.append("Items:")
        for item in items:
            lines.append(f"- {item}")

    if charges:
        lines.append("Charges:")
        for charge_name, amount in charges.items():
            lines.append(f"{charge_name.capitalize()}: {amount}")

    total = sum(charges.values(), 0.0)
    lines.append(f"Total Amount Due: {total}")
    return "\n".join(lines)
