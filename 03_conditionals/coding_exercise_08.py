def get_delivery_offer(bill_amount: float) -> str:
    if bill_amount > 500:
        return "You get a free dessert!"
    else:
        return "No free dessert this time."
