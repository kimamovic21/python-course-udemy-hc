customer = {"name": "John Doe", "age": 32, "city": "New York"}

print(customer)

customer["email"] = "john.doe@example.com"
customer["phone"] = "123-456-7890"

print(customer)

print(customer["name"])
print(customer["city"])

print("email" in customer)

del customer["age"]

print(customer)

print(customer.keys())
print(customer.values())
print(customer.items())

print(customer.popitem())

print(customer.get("membership"))

customer["address"] = "221B Baker Street"

print(customer)

print(customer)
