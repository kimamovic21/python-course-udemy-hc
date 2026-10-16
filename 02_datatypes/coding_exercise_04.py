my_cart = ["apples", "bananas", "milk"]
print(my_cart)

my_cart.append("bread")
print(my_cart)

my_cart.insert(0, "ketchup")
print(my_cart)

my_cart.remove("bananas")
print(my_cart)

removed_item = my_cart.pop()
print(removed_item)

my_cart.extend(["rice", "butter"])
print(my_cart)

my_cart.sort()
print(my_cart)

my_cart.reverse()
print(my_cart)

combined_cart = my_cart + ["juice", "jam"]
print(combined_cart)

duplicated_cart = my_cart * 2
print(duplicated_cart)

vegetables_text = "tomato cucumber spinach"
vegetables_list = vegetables_text.split()
print(vegetables_list)
