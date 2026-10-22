# 03 — Conditionals

This section introduces conditional logic with `if`, `elif`, `else`, nested conditions, comparisons, and `or`, using tea, snacks, customer billing, and device-status examples.

**Status: in progress.** This checkpoint covers four mini projects and coding exercises 07–10. More examples will be added as I continue the course.

## Learning order

**Start with Mini story 1: Is the Kettle Ready?** It is the first mini project in `03_conditionals`. Follow the order below even if your editor sorts the files differently:

1. **Mini project 1:** Read [MINI_STORY.md](MINI_STORY.md), then work through [mini_story_1.py](mini_story_1.py).
2. **Coding exercise 07:** Read [CODING_EXERCISE_07.md](CODING_EXERCISE_07.md), then work through [coding_exercise_07.py](coding_exercise_07.py).
3. **Mini project 2 — Snack Suggestion:** Read [SNAK_SUGESSTION.md](SNAK_SUGESSTION.md), then work through [snak_suggestion.py](snak_suggestion.py).
4. **Coding exercise 08:** Read [CODING_EXERCISE_08.md](CODING_EXERCISE_08.md), then work through [coding_exercise_08.py](coding_exercise_08.py).
5. **Mini project 3 — Chai Price Calculator:** Read [CHAI_PRICE_CALCULATOR.md](CHAI_PRICE_CALCULATOR.md), then work through [chai_price_calculator.py](chai_price_calculator.py).
6. **Coding exercise 09:** Read [CODING_EXERCISE_09.md](CODING_EXERCISE_09.md), then work through [coding_exercise_09.py](coding_exercise_09.py).
7. **Mini project 4 — Smart Thermostat:** Read [SMART_THERMOSTAT.md](SMART_THERMOSTAT.md), then work through [smart_thermostat.py](smart_thermostat.py).
8. **Coding exercise 10:** Read [CODING_EXERCISE_10.md](CODING_EXERCISE_10.md), then work through [coding_exercise_10.py](coding_exercise_10.py).

As more mini projects are added, their learning order and explanations will be documented here.

## Files covered so far

| File | Purpose |
| --- | --- |
| [MINI_STORY.md](MINI_STORY.md) | The kettle story, its tasks, and a change to try. |
| [mini_story_1.py](mini_story_1.py) | A boolean variable controlling a printed message with `if`. |
| [CODING_EXERCISE_07.md](CODING_EXERCISE_07.md) | The original Customer Discount Eligibility challenge, maintained manually. |
| [coding_exercise_07.py](coding_exercise_07.py) | Two independent `if` statements checking purchase amount and customer age. |
| [SNAK_SUGESSTION.md](SNAK_SUGESSTION.md) | The Snack Suggestion story, explanation, and example runs. |
| [snak_suggestion.py](snak_suggestion.py) | User input, lowercase conversion, `or`, and an `if`/`else` decision. |
| [CODING_EXERCISE_08.md](CODING_EXERCISE_08.md) | The original Restaurant Billing System challenge, maintained manually. |
| [coding_exercise_08.py](coding_exercise_08.py) | A function returning a dessert offer based on the bill amount. |
| [CHAI_PRICE_CALCULATOR.md](CHAI_PRICE_CALCULATOR.md) | The cup-pricing problem, solution explanation, and example runs. |
| [chai_price_calculator.py](chai_price_calculator.py) | An `if`/`elif`/`else` chain selecting a price from the requested cup size. |
| [CODING_EXERCISE_09.md](CODING_EXERCISE_09.md) | The original Delivery Charge Calculator challenge, maintained manually. |
| [coding_exercise_09.py](coding_exercise_09.py) | A function returning a delivery charge or an availability message based on distance. |
| [SMART_THERMOSTAT.md](SMART_THERMOSTAT.md) | The device-status problem, nested-condition explanation, and example results. |
| [smart_thermostat.py](smart_thermostat.py) | A nested `if` checking temperature only when the device is active. |
| [CODING_EXERCISE_10.md](CODING_EXERCISE_10.md) | The original Loan Eligibility Checker challenge, maintained manually. |
| [coding_exercise_10.py](coding_exercise_10.py) | Nested conditions checking the minimum age and income for loan eligibility. |

## Mini story 1: checking the kettle

Read the [story](MINI_STORY.md), then explore the [Python example](mini_story_1.py):

```python
kettle_boiled = True

if kettle_boiled:
    print("Kettle Done! time to make Chai")
```

`kettle_boiled` stores a boolean value. Since it is `True`, the indented `print()` runs:

```text
Kettle Done! time to make Chai
```

The colon starts the `if` block, and the four-space indentation shows which statement belongs to it. If `kettle_boiled` is changed to `False`, the block is skipped and this example prints nothing.

## Coding exercise 07: Customer Discount Eligibility

Read the [original challenge](CODING_EXERCISE_07.md) and the [Python solution](coding_exercise_07.py).

The program starts with `customer_name = "Amit"`, `customer_age = 24`, and `total_purchase = 1200`. It checks two conditions:

| Condition | Meaning | Result with the starting values |
| --- | --- | --- |
| `total_purchase > 1000` | The purchase must be strictly greater than 1000. | `True`: print `Eligible for discount`. |
| `customer_age >= 60` | The customer must be at least 60 years old. | `False`: skip the `Senior Citizen` message. |

Expected output:

```text
Eligible for discount
```

The two `if` statements are evaluated independently. A customer aged 60 or older with a purchase greater than 1000 would receive both messages. A purchase of exactly 1000 does not pass the discount condition.

`customer_name` stores the name requested by the challenge; it is not used in either condition.

## Mini project 2: Snack Suggestion

Read the [project description](SNAK_SUGESSTION.md) and the [Python example](snak_suggestion.py).

`input()` asks for a preferred snack and waits for the user to type an answer and press **Enter**. `.lower()` converts that answer to lowercase, so `Cookies` and `COOKIES` both become `cookies`.

The condition `snack == "cookies" or snack == "samosa"` is true when either comparison is true. The `if` block confirms an available snack; the `else` block handles other answers. Exactly one block runs.

Example with an available snack:

```text
Enter your preferred snack: Cookies
Great Choice! We'll serve you cookies
```

Example with another snack:

```text
Enter your preferred snack: chips
Sorry, we only serve cookies or samosa with tea
```

## Coding exercise 08: Restaurant Billing System

**Completed: Udemy test passed.**

Read the [original challenge](CODING_EXERCISE_08.md) and the [Python solution](coding_exercise_08.py).

The function `get_delivery_offer(bill_amount: float) -> str` accepts a bill amount and returns a message. Its name and parameter match the automatic test template.

| Bill amount | Returned string |
| --- | --- |
| Greater than `500` | `You get a free dessert!` |
| `500` or less | `No free dessert this time.` |

The condition uses `>`, so a bill of exactly `500` does not qualify. `return` sends the result back to the caller, where the automatic test can check it.

Example calls and their returned values:

```python
get_delivery_offer(500)     # "No free dessert this time."
get_delivery_offer(500.01)  # "You get a free dessert!"
```

Running this file alone produces no terminal output because it defines the function without calling it. A call returns the string; `print(get_delivery_offer(500.01))` would display it.

## Mini project 3: Chai Price Calculator

Read the [problem and solution explanation](CHAI_PRICE_CALCULATOR.md) and the [Python example](chai_price_calculator.py).

The program reads a cup size and converts it to lowercase. An `if`/`elif`/`else` chain selects a price: `small` costs 10 rupees, `medium` costs 15, and `large` costs 20. Other answers produce `Unknown cup size`.

Conditions are checked in order. Once one matches, its block runs and the remaining branches are skipped, so each run prints one message.

## Coding exercise 09: Delivery Charge Calculator

Read the [original challenge](CODING_EXERCISE_09.md) and the [Python solution](coding_exercise_09.py).

The function `calculate_delivery_charge(distance: float) -> str` receives a distance in kilometres and returns the appropriate message:

| Distance | Returned string |
| --- | --- |
| 2 km or less | `Delivery charge: 0` |
| More than 2 km, up to and including 5 km | `Delivery charge: 30` |
| More than 5 km, up to and including 10 km | `Delivery charge: 50` |
| More than 10 km | `Delivery not available for your location.` |

The `if`/`elif`/`else` chain checks the ranges in order. When execution reaches `elif distance <= 5`, the first condition was false, so the distance is already greater than 2. A matching branch uses `return` to send its message back to the caller and end the function.

Example calls and their returned values:

```python
calculate_delivery_charge(2)      # "Delivery charge: 0"
calculate_delivery_charge(2.01)   # "Delivery charge: 30"
calculate_delivery_charge(10)     # "Delivery charge: 50"
calculate_delivery_charge(10.01)  # "Delivery not available for your location."
```

Automatic tests provide the distance through the function parameter. To display a returned message, a caller can use `print(calculate_delivery_charge(5))`, which prints `Delivery charge: 30`.

## Mini project 4: Smart Thermostat

Read the [problem and solution explanation](SMART_THERMOSTAT.md) and the [Python example](smart_thermostat.py).

The outer `if` checks whether `device_status` is `"active"`. Only then does the inner `if` check whether `temperature > 35`. Higher values produce an alert; values of `35` or less produce the normal-temperature message. Other device statuses produce `Device is offline`.

Each `else` lines up with the `if` it belongs to. With the starting values `"active"` and `38`, the output is:

```text
High temperature alert!
```

## Coding exercise 10: Loan Eligibility Checker

Read the [original challenge](CODING_EXERCISE_10.md) and the [Python solution](coding_exercise_10.py).

The function `check_loan_eligibility(age: int, income: float) -> str` checks the customer's age first. If the customer is at least 21, a nested `if` checks whether their income is at least `25_000`.

| Age | Income | Returned string |
| --- | --- | --- |
| Less than 21 | Any amount | `Not eligible: Age must be 21 or above` |
| 21 or above | Less than `25_000` | `Not eligible: Income too low` |
| 21 or above | `25_000` or above | `Eligible for loan` |

Both checks use `>=`, so an age of exactly 21 and an income of exactly `25_000` qualify. Customers younger than 21 receive the age message before the income check is reached.

Example calls and their returned values:

```python
check_loan_eligibility(20, 30_000)  # "Not eligible: Age must be 21 or above"
check_loan_eligibility(21, 24_999)  # "Not eligible: Income too low"
check_loan_eligibility(21, 25_000)  # "Eligible for loan"
```

`return` sends the message back to the caller. For example, `print(check_loan_eligibility(21, 25_000))` displays `Eligible for loan`.

## How to run these examples

Open the repository root in VS Code, select your Python interpreter, and open the example you want to run. Press **Ctrl + S** to format and run it using the project's editor settings.

Alternatively, run these commands from the repository root:

```powershell
python 03_conditionals/mini_story_1.py
python 03_conditionals/coding_exercise_07.py
python 03_conditionals/snak_suggestion.py
python 03_conditionals/chai_price_calculator.py
python 03_conditionals/smart_thermostat.py
```

For Snack Suggestion, type your answer in the terminal when prompted and press **Enter**. Exercises 08–10 define functions: use the provided automatic tests or call the functions as described above. Running these function files alone produces no terminal output.

For Chai Price Calculator, enter a cup size when prompted and press **Enter**.

The examples use features included with Python. See the [main README](../README.md#quick-start) for editor setup.
