# 04 — Loops

This section introduces `for` and `while` loops, number ranges, list iteration, numbering with `enumerate()`, and pairing values with `zip()`. Later examples use `continue`, `break`, and `for`/`else` to control how loops finish. The latest examples introduce the walrus operator (`:=`) and dictionary lookups for customer discounts.

**Status: in progress.** This checkpoint covers ten numbered examples and coding exercises 13–18. More lessons will be added as I continue the course.

## Learning order

1. Start with [01_token_dispenser.py](01_token_dispenser.py) to repeat an action for tokens 1–10.
2. Continue with [02_batch_chai.py](02_batch_chai.py) to prepare four batches of chai.
3. Read the [original challenge 13](CODING_EXERCISE_13.md), then explore [coding_exercise_13.py](coding_exercise_13.py).
4. Continue with [03_tea_orders.py](03_tea_orders.py) to iterate directly over a list of names.
5. Read the [original challenge 14](CODING_EXERCISE_14.md), then explore [coding_exercise_14.py](coding_exercise_14.py).
6. Continue with [04_tea_menu.py](04_tea_menu.py) to number menu items using `enumerate()`.
7. Read the [original challenge 15](CODING_EXERCISE_15.md), then explore [coding_exercise_15.py](coding_exercise_15.py).
8. Continue with [05_order_summary.py](05_order_summary.py) to pair customer names with their bills using `zip()`.
9. Read the [original challenge 16](CODING_EXERCISE_16.md), then explore [coding_exercise_16.py](coding_exercise_16.py).
10. Continue with [06_tea-temperature.py](06_tea-temperature.py) to repeat a temperature check using `while`.
11. Read the [original challenge 17](CODING_EXERCISE_17.md), then explore [coding_exercise_17.py](coding_exercise_17.py).
12. Continue with [07_put_of_order.py](07_put_of_order.py) to skip unavailable items and stop at a discontinued item.
13. Continue with [08_for_else.py](08_for_else.py) to use a loop's `else` when a search finishes without `break`.
14. Read the [original challenge 18](CODING_EXERCISE_18.md), then explore [coding_exercise_18.py](coding_exercise_18.py).
15. Continue with [09_walrus.py](09_walrus.py) to assign and check values with `:=`, then repeat input until an available flavour is chosen.
16. Continue with [10_dictionary_case.py](10_dictionary_case.py) to look up coupon rules and calculate each customer's next-visit discount.

Follow this order even if your editor sorts the files differently. The numbered examples are explained below.

## Files covered so far

| File | Purpose |
| --- | --- |
| [01_token_dispenser.py](01_token_dispenser.py) | A `for` loop printing a message for each token number. |
| [02_batch_chai.py](02_batch_chai.py) | A `for` loop printing a message for each batch. |
| [CODING_EXERCISE_13.md](CODING_EXERCISE_13.md) | The original Generate Multiplication Table challenge, maintained manually. |
| [coding_exercise_13.py](coding_exercise_13.py) | A function building and returning a list of multiplication-table strings. |
| [03_tea_orders.py](03_tea_orders.py) | A `for` loop reading names directly from a list and printing order-ready messages. |
| [CODING_EXERCISE_14.md](CODING_EXERCISE_14.md) | The original Task Completion Tracker challenge, maintained manually. |
| [coding_exercise_14.py](coding_exercise_14.py) | A function returning a new list of tasks prefixed with `Completed: `. |
| [04_tea_menu.py](04_tea_menu.py) | Numbering menu items with `enumerate(menu, start=1)`. |
| [CODING_EXERCISE_15.md](CODING_EXERCISE_15.md) | The original Numbered Task List challenge, maintained manually. |
| [coding_exercise_15.py](coding_exercise_15.py) | A function returning a new list of tasks numbered from 1. |
| [05_order_summary.py](05_order_summary.py) | Pairing customer names and bill amounts with `zip()` and printing payment summaries. |
| [CODING_EXERCISE_16.md](CODING_EXERCISE_16.md) | The original Student Scores Report challenge, maintained manually. |
| [coding_exercise_16.py](coding_exercise_16.py) | A function pairing student names and scores into a new list of report strings. |
| [06_tea-temperature.py](06_tea-temperature.py) | Repeating temperature messages with `while` and updating the temperature using `+=`. |
| [CODING_EXERCISE_17.md](CODING_EXERCISE_17.md) | The original ATM Withdrawal Simulator challenge, maintained manually. |
| [coding_exercise_17.py](coding_exercise_17.py) | A function processing withdrawal requests with `while` and returning messages plus the final balance. |
| [07_put_of_order.py](07_put_of_order.py) | Skipping an out-of-stock flavour with `continue` and stopping at a discontinued flavour with `break`. |
| [08_for_else.py](08_for_else.py) | Finding the first eligible staff member and using `for`/`else` when no match is found. |
| [CODING_EXERCISE_18.md](CODING_EXERCISE_18.md) | The original Parcel Scanning System challenge, maintained manually. |
| [coding_exercise_18.py](coding_exercise_18.py) | A function combining `continue`, `break`, and `for`/`else` to return parcel scan messages. |
| [09_walrus.py](09_walrus.py) | Assigning values within conditions using `:=` and asking for an available chai flavour with `while`. |
| [10_dictionary_case.py](10_dictionary_case.py) | Looking up coupon rules with `.get()`, unpacking tuples, and calculating discounts for a list of customers. |

## Example 01: Token Dispenser

```python
for token in range(1, 11):
    print(f"Serving chai to Token #{token}")
```

`range(1, 11)` supplies the numbers **1 through 10**. The start is included; the stop value, `11`, is excluded.

On each iteration, `token` receives the next number and the indented `print()` runs. The f-string inserts the current token number into the message.

Expected output:

```text
Serving chai to Token #1
Serving chai to Token #2
Serving chai to Token #3
Serving chai to Token #4
Serving chai to Token #5
Serving chai to Token #6
Serving chai to Token #7
Serving chai to Token #8
Serving chai to Token #9
Serving chai to Token #10
```

## Example 02: Batch Chai

```python
for batch in range(1, 5):
    print(f"Preparing chai for batch #{batch}")
```

`range(1, 5)` supplies **1, 2, 3, and 4**, so the loop runs four times. Each iteration assigns the next number to `batch` and prints a message.

Expected output:

```text
Preparing chai for batch #1
Preparing chai for batch #2
Preparing chai for batch #3
Preparing chai for batch #4
```

In both examples, the colon starts the loop block and four-space indentation shows which statement repeats.

## Coding exercise 13: Generate Multiplication Table

**Completed: Udemy test passed.**

Read the [original challenge](CODING_EXERCISE_13.md) and the [Python solution](coding_exercise_13.py).

The function `multiplication_table(number: int) -> list[str]` receives an integer and returns a list of ten strings:

1. Create an empty list, `table = []`.
2. Loop through multipliers 1–10 with `range(1, 11)`.
3. Build each string with `f"{number} x {multiplier} = {number * multiplier}"` and add it to the list using `.append()`.
4. Return the complete list after the loop finishes.

For `multiplication_table(3)`, selected entries from the returned list are:

| Multiplier | String |
| --- | --- |
| `1` | `"3 x 1 = 3"` |
| `4` | `"3 x 4 = 12"` |
| `10` | `"3 x 10 = 30"` |

`return table` is outside the loop, so all ten strings are collected before the function returns. The spaces and lowercase `x` match the challenge's required format.

## Example 03: Tea Orders

```python
orders = ["Hitesh", "Aman", "Becky", "Carlos"]

for name in orders:
    print(f"Order ready for {name}")
```

This loop reads values directly from the `orders` list. On each iteration, `name` receives the next customer's name, following the list's order. The f-string inserts that name into the message.

Expected output:

```text
Order ready for Hitesh
Order ready for Aman
Order ready for Becky
Order ready for Carlos
```

## Coding exercise 14: Task Completion Tracker

Read the [original challenge](CODING_EXERCISE_14.md) and the [Python solution](coding_exercise_14.py).

The function `mark_completed_tasks(tasks: list[str]) -> list[str]` creates an empty `completed_tasks` list, then visits each task with `for task in tasks`. Each iteration builds `f"Completed: {task}"` and adds it to the new list using `.append()`.

`return completed_tasks` runs after the loop. The function preserves the original list and its order; an empty input list produces an empty result list.

For `mark_completed_tasks(["Buy groceries", "Pay bills", "Call mom"])`, the returned value is:

```python
[
    "Completed: Buy groceries",
    "Completed: Pay bills",
    "Completed: Call mom",
]
```

Use exactly **one space** after `Completed:` to match the expected test output. Automated tests compare the complete strings, including spaces.

## Example 04: Tea Menu

```python
menu = ["Green", "Lemon", "Spiced", "Mint"]

for idx, item in enumerate(menu, start=1):
    print(f"{idx} : {item} chai")
```

`enumerate(menu, start=1)` provides a number and a menu item on each iteration. The loop assigns them to `idx` and `item`, then inserts both into the printed message.

The counter starts at 1 for display. This does not change the list's indexes, which still start at 0.

Expected output:

```text
1 : Green chai
2 : Lemon chai
3 : Spiced chai
4 : Mint chai
```

## Coding exercise 15: Numbered Task List

**Completed: Udemy test passed.**

Read the [original challenge](CODING_EXERCISE_15.md) and the [Python solution](coding_exercise_15.py).

The function `generate_numbered_tasks(tasks: list[str]) -> list[str]` creates an empty `numbered_tasks` list and loops through `enumerate(tasks, start=1)`. Each iteration appends `f"{number}. {task}"` to the new list.

For `generate_numbered_tasks(["Buy groceries", "Pay bills", "Call mom"])`, the returned value is:

```python
[
    "1. Buy groceries",
    "2. Pay bills",
    "3. Call mom",
]
```

Each string contains a number, a period, and exactly one space before the task name. The function preserves the original task list and its order. An empty input list produces an empty result list.

`return numbered_tasks` runs after the loop, once all tasks have been added.

## Example 05: Order Summary

```python
names = ["Hitesh", "Meera", "Sam", "Ali"]
bills = [50, 70, 100, 55]

for name, amount in zip(names, bills):
    print(f"{name} paid {amount} rupees")
```

`zip(names, bills)` pairs values at the same position: `Hitesh` with `50`, `Meera` with `70`, and so on. On each iteration, the loop assigns the current pair to `name` and `amount`, then prints the payment summary.

Expected output:

```text
Hitesh paid 50 rupees
Meera paid 70 rupees
Sam paid 100 rupees
Ali paid 55 rupees
```

With ordinary `zip()`, iteration stops when the shorter input ends. This example has four names and four amounts, so all four pairs are processed.

## Coding exercise 16: Student Scores Report

**Completed: Udemy test passed.**

Read the [original challenge](CODING_EXERCISE_16.md) and the [Python solution](coding_exercise_16.py).

The function `generate_score_report(names: list[str], scores: list[int]) -> list[str]` creates an empty `report` list, then loops through `zip(names, scores)`. Each iteration appends `f"{name} scored {score} marks"` to the new list.

For `generate_score_report(["Alice", "Bob", "John Doe"], [95, 0, 100])`, the returned value is:

```python
[
    "Alice scored 95 marks",
    "Bob scored 0 marks",
    "John Doe scored 100 marks",
]
```

The original names and scores remain unchanged. The report follows their paired order, and `return report` runs after the loop. An empty input produces no pairs and returns an empty list; lists of different lengths produce entries only for the available pairs.

## Example 06: Tea Temperature

```python
temperature = 40

while temperature < 100:
    print(f"Current temperature: {temperature}")
    temperature += 15

print("Tea is ready to boil")
```

`while` checks its condition before each iteration. The loop starts at `40`, prints the current value, and increases it by `15`. `temperature += 15` means the same as `temperature = temperature + 15`.

The values printed inside the loop are `40`, `55`, `70`, and `85`. After the last increase, the temperature becomes `100`, so `temperature < 100` is false and the loop ends. The final `print()` is outside the loop and runs once.

Expected output:

```text
Current temperature: 40
Current temperature: 55
Current temperature: 70
Current temperature: 85
Tea is ready to boil
```

## Coding exercise 17: ATM Withdrawal Simulator

**Completed: Udemy test passed.**

Read the [original challenge](CODING_EXERCISE_17.md) and the [Python solution](coding_exercise_17.py).

The function `simulate_atm_withdrawals(balance: int, withdrawals: list[int]) -> list[str]` processes requests in order and returns a list of messages:

1. Start with an empty `messages` list and `index = 0`.
2. While `index < len(withdrawals)`, read the amount at `withdrawals[index]`.
3. If `balance >= amount`, subtract it and append `Withdrawn: {amount}`. Otherwise, append `Insufficient funds for requested amount: {amount}` and keep the current balance.
4. Increase `index` after either outcome so the next request is processed.
5. After the loop, append `Remaining Balance: {balance}` once and return the messages.

For `simulate_atm_withdrawals(100, [40, 80, 20])`, the returned value is:

```python
[
    "Withdrawn: 40",
    "Insufficient funds for requested amount: 80",
    "Withdrawn: 20",
    "Remaining Balance: 40",
]
```

After the first withdrawal, `60` remains. The request for `80` is rejected, so the next request for `20` can still succeed. A request equal to the current balance also succeeds because the condition uses `>=`.

The original withdrawal list stays unchanged. An empty list returns just the final-balance message, for example `["Remaining Balance: 500"]` when the starting balance is `500`.

## Example 07: Stock Availability

Read [07_put_of_order.py](07_put_of_order.py). The loop visits the flavours in order and handles two special values:

- `"Out of Stock"` triggers `continue`, which skips the rest of that iteration and moves to the next flavour.
- `"Discontinued"` prints a message and triggers `break`, which ends the loop immediately.

With the starting list, `Ginger` and `Lemon` are printed. The discontinued item is printed before the break, and `Tulsi` is never reached. The final statement outside the loop still runs.

Expected output:

```text
Ginger item found
Lemon item found
Discontinued item found
Out side of loop
```

## Example 08: For-Else Search

Read [08_for_else.py](08_for_else.py). Each entry in `staff` is a tuple containing a name and an age. `for name, age in staff` unpacks each pair, then checks whether `age >= 18`.

When the loop finds an eligible person, it prints their name and uses `break` to end the search. With the starting values, Amit is 26, so the output is:

```text
Amit is eligible to manage the staff.
```

The `else` lines up with `for` and belongs to the loop. It runs when iteration finishes without `break`. If every person is younger than 18, the output is `No one eligible to manage the staff.` An empty staff list also reaches this `else`.

## Coding exercise 18: Parcel Scanning System

**Completed: Udemy tests passed.**

Read the [original challenge](CODING_EXERCISE_18.md) and the [Python solution](coding_exercise_18.py).

The function `scan_parcels(parcel_codes: list[str]) -> list[str]` builds a new list of scan messages:

| Barcode | Action | Message |
| --- | --- | --- |
| `"DAMAGED"` | Log the issue, then skip this parcel with `continue`. | `Skipped damaged parcel` |
| `"STOP"` | Log the error, then end the loop with `break`. | `Critical error: Stopping scan` |
| Any other barcode | Log the scanned parcel. | `Scanned parcel: <barcode>` |

If the loop finishes without `break`, its `else` appends `All parcels scanned successfully`. Skipping damaged parcels with `continue` still allows this final message when iteration reaches the end.

For `scan_parcels(["P001", "DAMAGED", "P002"])`, the returned value is:

```python
[
    "Scanned parcel: P001",
    "Skipped damaged parcel",
    "Scanned parcel: P002",
    "All parcels scanned successfully",
]
```

For `scan_parcels(["P001", "STOP", "P002"])`, scanning stops before `P002` and the returned value is:

```python
[
    "Scanned parcel: P001",
    "Critical error: Stopping scan",
]
```

The function leaves the original parcel list unchanged. An empty list returns `["All parcels scanned successfully"]` because the loop finishes without a break.

## Example 09: Walrus Operator

Read [09_walrus.py](09_walrus.py). The walrus operator, `:=`, assigns a value to a variable and makes that value available in the surrounding expression.

```python
value = 13

if remainder := value % 5:
    print(f"Not divisible, remainder is {remainder}")
```

`13 % 5` gives the remainder `3`. The condition stores it in `remainder`, then checks its truth value. A nonzero number is truthy, so the message is printed. A remainder of `0` is falsy and would skip this block.

The second active example offers `masala`, `ginger`, `lemon`, and `mint`, then validates the user's choice:

```python
while (flavor := input("Choose your flavor: ")) not in flavors:
    print(f"Sorry, {flavor} is not available")

print(f"You choose {flavor} chai")
```

Each condition check reads input and saves it in `flavor`. An unavailable choice runs the loop body and prompts again. An available choice ends the loop, and the final message uses the saved value. The input must match a listed flavour exactly, including lowercase letters.

Example terminal session, entering `vanilla` and then `ginger`:

```text
Not divisible, remainder is 3
Available flavors:  ['masala', 'ginger', 'lemon', 'mint']
Choose your flavor: vanilla
Sorry, vanilla is not available
Choose your flavor: ginger
You choose ginger chai
```

The file also contains commented examples of separate assignment and a cup-size check. Lines starting with `#` do not run.

## Example 10: Dictionary-Based Discounts

Read [10_dictionary_case.py](10_dictionary_case.py). `users` is a list of dictionaries, each holding a customer's `id`, purchase `total`, and `coupon` code. `discounts` maps each coupon code to a tuple containing `(percent, fixed)`.

The loop processes one customer at a time:

```python
for user in users:
    percent, fixed = discounts.get(user["coupon"], (0, 0))
    discount = user["total"] * percent + fixed
```

`user["coupon"]` reads the current customer's coupon code. `.get()` finds its rule, and tuple unpacking assigns the two values to `percent` and `fixed`. If the coupon is missing from `discounts`, `.get()` returns the default `(0, 0)`, giving no discount.

With the current values:

| User | Total | Coupon | Rule `(percent, fixed)` | Discount calculation |
| --- | --- | --- | --- | --- |
| `1` | `100` | `P20` | `(0.2, 0)` | `100 * 0.2 + 0 = 20.0` |
| `2` | `150` | `F10` | `(0.5, 0)` | `150 * 0.5 + 0 = 75.0` |
| `3` | `80` | `P50` | `(0, 10)` | `80 * 0 + 10 = 10` |

Coupon names are labels; their tuple values determine the actual discount. In this example, `F10` gives 50% and `P50` gives a fixed 10 rupees.

Expected output:

```text
User 1 paid total 100 and got discount for next visit of rupees 20.0
User 2 paid total 150 and got discount for next visit of rupees 75.0
User 3 paid total 80 and got discount for next visit of rupees 10
```

The discount is reported for the next visit. The code does not subtract it from the current purchase total or change the customer dictionaries.

## How to run these examples

Open the repository root in VS Code, select your Python interpreter, and open an example. Press **Ctrl + S** to format and run it using the project's editor settings.

Alternatively, run the numbered examples from the repository root:

```powershell
python 04_loops/01_token_dispenser.py
python 04_loops/02_batch_chai.py
python 04_loops/03_tea_orders.py
python 04_loops/04_tea_menu.py
python 04_loops/05_order_summary.py
python 04_loops/06_tea-temperature.py
python 04_loops/07_put_of_order.py
python 04_loops/08_for_else.py
python 04_loops/09_walrus.py
python 04_loops/10_dictionary_case.py
```

`09_walrus.py` waits for terminal input. Enter an available lowercase flavour, such as `ginger`, to finish the script.

Exercises 13–18 define functions for automatic testing. The tests supply the function arguments and check the returned lists. Running these files alone defines the functions without displaying a result. After loading a function, a caller can use `print(scan_parcels(["P001", "DAMAGED", "P002"]))` to display its result.

See the [main README](../README.md#quick-start) for editor setup. These examples use features included with Python.
