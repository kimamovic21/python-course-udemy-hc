branch_a_products = {"bread", "milk", "butter", "jam"}
branch_b_products = {"bread", "cheese", "butter", "ketchup"}

print(f"Branch A products: {branch_a_products}")
print(f"Branch B products: {branch_b_products}")

print(f"Union of both branches: {branch_a_products | branch_b_products}")
print(f"Intersection of both branches: {branch_a_products & branch_b_products}")
print(f"Products only in branch A: {branch_a_products - branch_b_products}")

print(f"Is ketchup available in branch A? {'ketchup' in branch_a_products}")

essential_items = frozenset({"milk", "bread", "ketchup"})
print(f"Essential items (frozenset): {essential_items}")
