# This function will be tested automatically.
# Do not change the function name or parameters.


"""
items: A list of dictionaries, each representing a product with keys:
    - "name": str
    - "price": int
    - "category": str

Returns:
    - List of names of affordable products (price < 500)
    - Set of unique categories
    - Dictionary of product name to price mapping
    - Generator expression converted to list of prices after applying 10% discount
"""


def filter_inventory(
    items: list[dict],
) -> tuple[list[str], set[str], dict[str, int], list[float]]:
    # Write your code below this line
    affordable_names = [item["name"] for item in items if item["price"] < 500]
    categories = {item["category"] for item in items}
    name_to_price = {item["name"]: item["price"] for item in items}
    discounted_prices = list(item["price"] * 0.9 for item in items)

    return affordable_names, categories, name_to_price, discounted_prices
