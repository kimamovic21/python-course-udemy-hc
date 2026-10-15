is_boiling = True
stir_count = 5
total_actions = stir_count + is_boiling  # True counts as 1 in arithmetic
print(f"Total actions: {total_actions}")

milk_present = 0  # No milk
print(f"Is there milk? {bool(milk_present)}")

water_hot = True
tea_added = True

can_serve = water_hot and tea_added
print(f"Can we serve chai? {can_serve}")
