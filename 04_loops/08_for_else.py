staff = [("Amit", 26), ("Zara", 17), ("Raj", 15)]

for name, age in staff:
    if age >= 18:
        print(f"{name} is eligible to manage the staff.")
        break
else:
    print(f"No one eligible to manage the staff.")
