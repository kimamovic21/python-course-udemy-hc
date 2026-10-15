# Integers

black_tea_grams = 14
ginger_grams = 3

total_grams = black_tea_grams + ginger_grams
print(f"Total weight of the tea base: {total_grams} grams")

remaining_tea = black_tea_grams - ginger_grams
print(f"Remaining tea: {remaining_tea} grams")

milk_litres = 7
servings = 4
milk_per_serving = milk_litres / servings
print(f"Milk per serving: {milk_per_serving} litres")

total_tea_bags = 7
pots = 4
bags_per_pot = total_tea_bags // pots
print(f"Whole tea bags per pot: {bags_per_pot}")

total_cardamom_pods = 10
pods_per_cup = 3
leftover_pods = total_cardamom_pods % pods_per_cup
print(f"Leftover cardamom pods: {leftover_pods}")

base_flavour_strength = 2
scale_factor = 3
powerful_flavour = base_flavour_strength**scale_factor
print(f"Scaled flavour strength: {powerful_flavour}")
# 2 * 2 * 2

total_tea_leaves_harvested = 1_000_000_000
print(f"Tea leaves: {total_tea_leaves_harvested}")
