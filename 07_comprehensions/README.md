# 07 — Comprehensions

This section introduces list, set, and dictionary comprehensions, as well as generator expressions. The examples filter a menu, collect unique values, convert prices, and sum selected sales. Exercise 23 combines these ideas in an inventory filter.

**Status: completed.** This section covers four numbered examples, coding exercise 23, and the review quiz. The exercise implementation has been checked locally.

## Learning order

1. Start with [01_list_compre.py](01_list_compre.py) to filter menu items using a list comprehension.
2. Continue with [02_set_compre.py](02_set_compre.py) to collect unique chai names and ingredients.
3. Continue with [03_dict_compre.py](03_dict_compre.py) to build a dictionary of converted prices.
4. Continue with [04_genrator_compre.py](04_genrator_compre.py) to sum selected sales using a generator expression.
5. Read the [original challenge 23](CODING_EXERCISE_23.md), then explore [coding_exercise_23.py](coding_exercise_23.py) to return four inventory summaries.

Follow this order even if your editor sorts the files differently. The numbered examples are explained below.

## Files covered so far

| File | Purpose |
| --- | --- |
| [01_list_compre.py](01_list_compre.py) | Creating and printing a new list of menu items containing `"Iced"`. |
| [02_set_compre.py](02_set_compre.py) | Removing duplicate chai names and collecting unique ingredients from recipe lists. |
| [03_dict_compre.py](03_dict_compre.py) | Keeping tea names as keys while converting their prices using a fixed divisor. |
| [04_genrator_compre.py](04_genrator_compre.py) | Feeding sales greater than 5 into `sum()` through a generator expression. |
| [CODING_EXERCISE_23.md](CODING_EXERCISE_23.md) | The original Smart Inventory Filter challenge, maintained manually. |
| [coding_exercise_23.py](coding_exercise_23.py) | Returning affordable names, unique categories, a name-to-price mapping, and discounted prices. |

## Example 01: Filtering Iced Teas

Read [01_list_compre.py](01_list_compre.py).

```python
menu = [
    "Masala Chai",
    "Iced Lemon Tea",
    "Green Tea",
    "Iced Peach Tea",
    "Ginger chai",
]

iced_tea = [my_tea for my_tea in menu if "Iced" in my_tea]

print(iced_tea)
```

`menu` contains five strings. The comprehension visits each one, checks whether it contains `"Iced"`, and collects the matching strings into a new list called `iced_tea`.

| Part | Meaning |
| --- | --- |
| `my_tea` at the beginning | The value to put in the new list when the condition is true. |
| `for my_tea in menu` | Visit each menu item in order. |
| `if "Iced" in my_tea` | Keep only strings containing the substring `"Iced"`. |

The check is case-sensitive: `"Iced"` and `"iced"` are different. The new list preserves the order of matching items, and the original `menu` stays unchanged.

The same filtering logic can be written as a regular loop:

```python
iced_tea = []
for my_tea in menu:
    if "Iced" in my_tea:
        iced_tea.append(my_tea)
```

Expected output from the script:

```text
['Iced Lemon Tea', 'Iced Peach Tea']
```

The trailing comma after `"Ginger chai"` keeps the menu laid out with one item per line when Black formats the file.

## Example 02: Unique Chais and Ingredients

Read [02_set_compre.py](02_set_compre.py). The first set comprehension collects each chai name once:

```python
unique_chai = {chai for chai in favorite_chais}
```

Sets contain unique elements, so repeated `"Masala Chai"` and `"Green Tea"` entries appear only once in the result.

The second comprehension visits the ingredient lists in `recipes`:

```python
unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}
```

Read the two `for` clauses from left to right: first take an ingredient list from `recipes.values()`, then visit each spice in that list. The set collects each ingredient once across all recipes.

One possible output is shown below. **Set display order can vary**; the elements are what matter.

```text
{'Masala Chai', 'Green Tea', 'Lemon Tea', 'Elaichi Chai'}
{'ginger', 'cardamom', 'clove', 'milk', 'black pepper'}
```

## Example 03: Converting Prices with a Dictionary Comprehension

Read [03_dict_compre.py](03_dict_compre.py).

```python
tea_prices_usd = {tea: price / 80 for tea, price in tea_prices_inr.items()}
```

`.items()` provides each tea name and its price. The comprehension keeps the name as the key and uses `price / 80` as the new value.

The script uses a fixed practice rate of 80 INR per USD. For example, `40 / 80` gives `0.5`. The original price dictionary stays unchanged.

Expected output:

```text
{'Masala Chai': 0.5, 'Green Tea': 0.625, 'Lemon Tea': 2.5}
```

## Example 04: Summing Sales with a Generator Expression

Read [04_genrator_compre.py](04_genrator_compre.py).

```python
total_cups = sum(sale for sale in daily_sales if sale > 5)
```

The generator expression produces each matching sale as `sum()` consumes it. The condition is strictly greater than 5, so the values `5` and `3` are excluded.

The selected values are `10`, `12`, `7`, `8`, `9`, and `15`. Their sum is `61`. Values are produced on demand, so this calculation can run without building an intermediate list.

Expected output:

```text
61
```

## Coding exercise 23: Smart Inventory Filter

**Implemented and checked locally.**

Read the [original challenge](CODING_EXERCISE_23.md) and the [Python solution](coding_exercise_23.py).

`filter_inventory(items)` receives a list of product dictionaries containing `name`, `price`, and `category`. It returns a tuple with four results, in this order:

| Result | Technique | Contents |
| --- | --- | --- |
| `affordable_names` | List comprehension | Names of products priced strictly below `500`. |
| `categories` | Set comprehension | All unique product categories. |
| `name_to_price` | Dictionary comprehension | A mapping from each product name to its price. |
| `discounted_prices` | Generator expression converted with `list()` | All product prices after a 10% discount, calculated as `price * 0.9`. |

The function processes the supplied products and leaves them unchanged. A price of exactly `500` is excluded from `affordable_names`; the other results still include that product. An empty input returns `([], set(), {}, [])`.

After loading the function, this example:

```python
products = [
    {"name": "Notebook", "price": 250, "category": "Stationery"},
    {"name": "Pen", "price": 100, "category": "Stationery"},
    {"name": "Bag", "price": 1200, "category": "Accessories"},
]

affordable_names, categories, name_to_price, discounted_prices = filter_inventory(
    products
)
print(affordable_names)
print(categories)
print(name_to_price)
print(discounted_prices)
```

displays the following values. The category set's display order can vary.

```text
['Notebook', 'Pen']
{'Stationery', 'Accessories'}
{'Notebook': 250, 'Pen': 100, 'Bag': 1200}
[225.0, 90.0, 1080.0]
```

The `10%` discount applies to every product, including those above the affordability threshold. Discounted amounts can be decimal numbers.

## Review: Choosing the Right Expression

| Expression | Example | Result |
| --- | --- | --- |
| List comprehension | `[x * x for x in range(1, 4)]` | A list containing `[1, 4, 9]`. |
| Set comprehension | `{x for x in [1, 2, 2, 3, 4] if x % 2 == 0}` | A set containing the unique even numbers `{2, 4}`. |
| Dictionary comprehension | `{x: x * x for x in range(1, 4)}` | A dictionary containing `{1: 1, 2: 4, 3: 9}`. |
| Generator expression | `(x for x in range(1, 4))` | A generator that produces `1`, `2`, and `3` on demand. |

List, set, and dictionary comprehensions build their collections immediately. A generator expression produces values as they are requested, which can reduce memory use when processing them one at a time.

## How to run these examples

Open the repository root in VS Code, select your Python interpreter, and open a numbered example. Press **Ctrl + S** to format and run it using the project's editor settings.

Alternatively, run the numbered examples from the repository root:

```powershell
python 07_comprehensions/01_list_compre.py
python 07_comprehensions/02_set_compre.py
python 07_comprehensions/03_dict_compre.py
python 07_comprehensions/04_genrator_compre.py
```

All four numbered scripts include `print()` calls and display the results described above.

`coding_exercise_23.py` defines a function for automatic testing. Running that file alone does not display a result. A caller supplies the products and uses the returned tuple, as shown in the exercise example.

See the [main README](../README.md#quick-start) for editor setup.
