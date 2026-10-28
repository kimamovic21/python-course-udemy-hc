# 05 — Functions

This section introduces functions, parameters, return values, code reuse, and variable scope. It also covers flexible arguments, early returns, tuple unpacking, pure and impure functions, recursion, and `lambda` with `filter()` and `map()`. The latest example explores docstrings, function metadata, and `help()`. Exercises 19–22 apply these ideas to student grade reports, loyalty points, invoices, and function behaviour.

**Status: in progress.** This checkpoint covers twelve numbered examples and coding exercises 19–22. More lessons will be added as I continue the course.

## Learning order

1. Start with [01_duplication.py](01_duplication.py) to define a function with parameters and reuse it for three chai orders.
2. Continue with [02_complex.py](02_complex.py) to build a workflow by calling smaller functions in order.
3. Continue with [03_hiding.py](03_hiding.py) to group registration steps behind a single function call.
4. Continue with [04_readability.py](04_readability.py) to return a calculated bill and use the result in different ways.
5. Continue with [05_trace.py](05_trace.py) to reuse a VAT calculation in a loop and inspect each result.
6. Read the [original challenge 19](CODING_EXERCISE_19.md), then explore [coding_exercise_19.py](coding_exercise_19.py) to calculate a grade and return a student report.
7. Continue with [06_scopes.py](06_scopes.py) to compare local, enclosing, and global variables with the same name.
8. Continue with [07_nonlocal.py](07_nonlocal.py) to update a variable belonging to an enclosing function.
9. Continue with [08_global_scope.py](08_global_scope.py) to update a module-level variable from a nested function.
10. Read the [original challenge 20](CODING_EXERCISE_20.md), then explore [coding_exercise_20.py](coding_exercise_20.py) to apply a bonus and accumulate loyalty points.
11. Continue with [09_input_params.py](09_input_params.py) to explore list mutation, positional and keyword arguments, extra arguments, and a `None` default.
12. Read the [original challenge 21](CODING_EXERCISE_21.md), then explore [coding_exercise_21.py](coding_exercise_21.py) to return an invoice with optional items and charges.
13. Continue with [10_return.py](10_return.py) to explore implicit `None`, early returns, and unpacking a returned tuple.
14. Continue with [11_types_of_functions.py](11_types_of_functions.py) to compare pure and impure functions, follow recursion, and filter a list with a lambda.
15. Read the [original challenge 22](CODING_EXERCISE_22.md), then explore [coding_exercise_22.py](coding_exercise_22.py) to practise pure, impure, recursive, and lambda-based functions.
16. Continue with [12_built_in.py](12_built_in.py) to inspect function documentation, use `help()`, and read a documented bill calculation.

Follow this order even if your editor sorts the files differently. The numbered examples are explained below.

## Files covered so far

| File | Purpose |
| --- | --- |
| [01_duplication.py](01_duplication.py) | Reusing `print_order(name, chai_type)` to display different orders without repeating the formatting logic. |
| [02_complex.py](02_complex.py) | Using `generate_report()` to call three smaller functions and display progress messages. |
| [03_hiding.py](03_hiding.py) | Using `register_user()` to coordinate input, validation, and saving steps represented by messages. |
| [04_readability.py](04_readability.py) | Returning a bill from `calculate_bill(cups, price_per_cup)` and using it in assignments and printed messages. |
| [05_trace.py](05_trace.py) | Returning a price including VAT and printing the original and final amounts for each order. |
| [CODING_EXERCISE_19.md](CODING_EXERCISE_19.md) | The original student grading challenge, maintained manually. |
| [coding_exercise_19.py](coding_exercise_19.py) | Reusing `calculate_grade(score)` inside `generate_student_report(name, score)` to return a formatted report. |
| [06_scopes.py](06_scopes.py) | Showing how separate local, enclosing, and global variables can share a name. |
| [07_nonlocal.py](07_nonlocal.py) | Updating an enclosing function's `chai_type` with `nonlocal`. |
| [08_global_scope.py](08_global_scope.py) | Updating the module-level `chai_type` with `global` inside a nested function. |
| [CODING_EXERCISE_20.md](CODING_EXERCISE_20.md) | The original Loyalty Points Tracker challenge, maintained manually. |
| [coding_exercise_20.py](coding_exercise_20.py) | Combining local totals, a nested bonus function, and global loyalty points. |
| [09_input_params.py](09_input_params.py) | Passing a mutable list, using positional and keyword arguments, collecting extra arguments, and creating a list from a `None` default. |
| [CODING_EXERCISE_21.md](CODING_EXERCISE_21.md) | The original Order Invoice Generator challenge, maintained manually. |
| [coding_exercise_21.py](coding_exercise_21.py) | Returning an invoice with a default customer name, variable items, and named charges. |
| [10_return.py](10_return.py) | Demonstrating implicit `None`, explicit and early returns, and unpacking three returned values. |
| [11_types_of_functions.py](11_types_of_functions.py) | Introducing pure and impure functions, recursive calls, and `lambda` with `filter()`. |
| [CODING_EXERCISE_22.md](CODING_EXERCISE_22.md) | The original Function Types challenge, maintained manually. |
| [coding_exercise_22.py](coding_exercise_22.py) | Adding numbers, updating a global counter, calculating a recursive factorial, and squaring a list with `map()`. |
| [12_built_in.py](12_built_in.py) | Reading `__doc__` and `__name__`, displaying `help(len)`, and documenting a bill function. |

## Example 01: Reusing an Order Function

Read [01_duplication.py](01_duplication.py).

```python
def print_order(name, chai_type):
    print(f"{name} ordered {chai_type} chai!")


print_order("Aman", "masala")
print_order("Hitesh", "Ginger")
print_order("Jia", "Tulsi")
```

`def` defines a function named `print_order`. The colon starts its body, and indentation marks the code belonging to it. Defining the function makes it available; its body runs each time it is called.

`name` and `chai_type` are **parameters**: names for the values the function receives. In `print_order("Aman", "masala")`, the strings `"Aman"` and `"masala"` are **arguments**: the actual values supplied to those parameters, in that order.

Each call runs the same `print()` statement with different values. The f-string inserts them into the message. Keeping the message format in one function means it can be changed in one place for all orders.

Expected output:

```text
Aman ordered masala chai!
Hitesh ordered Ginger chai!
Jia ordered Tulsi chai!
```

This function displays text with `print()`. It has no explicit `return` statement, so its return value is `None`.

## Example 02: Organising a Reporting Workflow

Read [02_complex.py](02_complex.py). The file defines three smaller functions and one function that coordinates them:

| Function | Role |
| --- | --- |
| `fetch_sales()` | Prints a message representing the data-fetching step. |
| `filter_valid_sales()` | Prints a message representing the filtering step. |
| `summarize_data()` | Prints a message representing the summarising step. |
| `generate_report()` | Calls the three functions in order, then prints the final report-ready message. |

The workflow is:

```python
def generate_report():
    fetch_sales()
    filter_valid_sales()
    summarize_data()
    print("Report is ready")


generate_report()
```

These functions take no arguments, so their definitions and calls use empty parentheses, `()`. The final `generate_report()` call starts the workflow. Its body calls each smaller function in sequence, waiting for each call to finish before moving to the next line.

The smaller functions currently represent their steps with printed messages. This example shows how splitting a larger task into named steps makes its structure easier to follow and update.

Expected output:

```text
Fetching the sales data
Filtering valid sales data
Summarizing sales data
Report is ready
```

## Example 03: Hiding Implementation Details

Read [03_hiding.py](03_hiding.py). A caller starts the registration workflow with one call to `register_user()`. That function handles the order of the smaller steps:

```python
def register_user():
    get_input()
    validate_input()
    save_to_db()
    print("User registration complete")


register_user()
```

`get_input()`, `validate_input()`, and `save_to_db()` are defined earlier in the file. Each currently prints a message representing its step. Calling `register_user()` keeps those details inside the function, so the caller can use the workflow by its name. This is a simple example of **abstraction**.

Expected output:

```text
Getting user input
Validating the user info
saving to database
User registration complete
```

## Example 04: Returning a Bill

Read [04_readability.py](04_readability.py).

```python
def calculate_bill(cups, price_per_cup):
    return cups * price_per_cup


my_bill = calculate_bill(3, 15)
print(my_bill)

print("Order for table 2: ", calculate_bill(2, 50))
```

`return` sends the calculated value back to the caller. The function name describes the calculation, and its parameters describe the two inputs.

The first call returns `3 * 15`, or `45`, which is stored in `my_bill` and then printed. The second call returns `2 * 50`, or `100`, directly inside `print()`. Returning a value lets the caller choose how to use it; displaying it is a separate step.

Expected output:

```text
45
Order for table 2:  100
```

There are two spaces before `100`: one at the end of the label string and one added by `print()` between its arguments.

## Example 05: Tracing a VAT Calculation

Read [05_trace.py](05_trace.py). `add_vat(price, vat_rate)` returns the full price including VAT, using the formula `price * (100 + vat_rate) / 100`.

For a price of `100` and a VAT rate of `10`, the calculation is `100 * 110 / 100 = 110.0`. The argument `10` represents 10%, so the result includes both the original price and the added tax.

The loop reuses this function for each order:

```python
orders = [100, 150, 200]

for price in orders:
    final_amount = add_vat(price, 10)
    print(f"Original: {price}, Final with VAT: {final_amount}")
```

On each iteration, `price` receives the next value, the function returns its amount including VAT, and `final_amount` stores that result. The printed pairs make it easy to trace how the calculation affects each order. Keeping the formula in one function also gives it one place to update.

Expected output:

```text
Original: 100, Final with VAT: 110.0
Original: 150, Final with VAT: 165.0
Original: 200, Final with VAT: 220.0
```

The results are floats because the formula uses `/` division.

## Coding exercise 19: Student Grading System

**Completed: Udemy tests passed.**

Read the [original challenge](CODING_EXERCISE_19.md) and the [Python solution](coding_exercise_19.py).

`calculate_grade(score)` checks score thresholds from highest to lowest and returns the matching letter:

| Score | Grade |
| --- | --- |
| `score >= 90` | `A` |
| `75 <= score < 90` | `B` |
| `60 <= score < 75` | `C` |
| `40 <= score < 60` | `D` |
| `score < 40` | `F` |

The `if`/`elif`/`else` chain selects one branch. Each branch uses `return` to send the grade back to the caller.

`generate_student_report(name, score)` calls `calculate_grade(score)`, stores the returned letter in `grade`, and returns an f-string containing the student's name, score, and grade. This keeps the grading rules in one function so they can be reused.

After loading the functions, this example call:

```python
print(generate_student_report("Aman", 80))
```

displays:

```text
Aman has scored 80 and received grade B
```

The functions return their results; the example caller uses `print()` to display the report. The wording and spacing of the returned string match the challenge's required format.

## Example 06: Variable Scope

Read [06_scopes.py](06_scopes.py). **Scope** describes where a variable name is available. Variables with the same name can belong to different scopes:

- In `serve_chai()`, the local `chai_type` is `"Masala"`. The module-level `chai_type` is `"Lemon"`, so the two messages use different values.
- In `chai_counter()`, `chai_order` is `"lemon"`. This is the enclosing scope for the nested `print_order()` function.
- `print_order()` assigns its own local `chai_order = "Ginger"`. That assignment leaves the enclosing value unchanged.
- The module-level `chai_order` is `"Tulsi"` and keeps its value after `chai_counter()` finishes.

Expected output:

```text
Inside function Masala
Outside function: Lemon
Inner: Ginger
Outer:  lemon
Global : Tulsi
```

## Example 07: Updating an Enclosing Variable

Read [07_nonlocal.py](07_nonlocal.py). The global `chai_type` starts as `"ginger"`, while `update_order()` defines a separate local `chai_type = "Elaichi"`.

Inside the nested `kitchen()` function, `nonlocal chai_type` selects the variable belonging to `update_order()`. Assigning `"Kesar"` updates that enclosing variable. After `kitchen()` returns, `update_order()` prints its new value:

```text
After kitchen update Kesar
```

The global `chai_type` remains `"ginger"`. `nonlocal` refers to a binding in an enclosing function scope.

## Example 08: Updating a Global Variable

Read [08_global_scope.py](08_global_scope.py). The module-level `chai_type` starts as `"Plain"`. Calling `front_desk()` calls its nested `kitchen()` function.

`global chai_type` inside `kitchen()` selects the module-level variable, so assigning `"Irani"` changes the value used by the final `print()` outside the functions.

Expected output:

```text
Final global chai:  Irani
```

## Coding exercise 20: Loyalty Points Tracker

**Completed: Udemy tests passed.**

Read the [original challenge](CODING_EXERCISE_20.md) and the [Python solution](coding_exercise_20.py).

`process_transactions(transactions: list[int]) -> int` receives one customer's transaction amounts and returns their final total:

1. `loyalty_points = 0` is defined at module level. `global loyalty_points` lets the function update that shared count.
2. `total = sum(transactions)` creates the local total for this customer.
3. The nested `apply_bonus()` uses `nonlocal total` to update that total. When it is strictly greater than `1000`, the function adds `50`. A total of exactly `1000` receives no bonus.
4. Calling `apply_bonus()` applies the rule before calculating points. `total // 100` awards one point per full 100 of the final amount, and `+=` adds those points to the global count.
5. `return total` returns the amount including any bonus. The accumulated points remain available in `loyalty_points`.

For `[400, 700]`, the sum is `1100`, the bonus makes it `1150`, and `1150 // 100` earns `11` points.

Starting with a fresh `loyalty_points` count of `0`, this example after loading the functions:

```python
print(process_transactions([400, 700]))
print(loyalty_points)
print(process_transactions([200, 300]))
print(loyalty_points)
```

displays:

```text
1150
11
500
16
```

The second customer earns another `5` points, giving `11 + 5 = 16`. The local `total` is calculated separately for each call, while the global points accumulate across calls during the same program run. An empty transaction list returns `0` and leaves the point count unchanged.

## Example 09: Input Parameters and Arguments

Read [09_input_params.py](09_input_params.py). The active code demonstrates several ways to pass and use arguments:

- **Mutable list:** `edit_chai(chai)` makes the parameter `cup` refer to the same list as `chai`. `cup[1] = 42` changes its second element, so the caller sees `[1, 42, 3]`.
- **Positional arguments:** `make_chai("Darjeeling", "Yes", "Low")` assigns values to `tea`, `milk`, and `sugar` in that order.
- **Keyword arguments:** `make_chai(tea="Green", sugar="Medium", milk="No")` matches arguments by name. The function still prints its parameters in the order `tea`, `milk`, `sugar`.
- **Extra positional arguments:** `*ingredients` collects `"Cinnamon"` and `"Cardamom"` into a tuple.
- **Extra keyword arguments:** `**extras` collects `sweetener="Honey"` and `foam="yes"` into a dictionary. The names `ingredients` and `extras` are chosen by the programmer; the common names `*args` and `**kwargs` work the same way.
- **Default argument:** `chai_order(order=None)` creates a fresh empty list when called without an argument. Each of the two calls prints `[]`.

Using `None` avoids sharing a mutable default list between calls. In the commented version with `order=[]`, the default list is created once when the function is defined, so repeated `.append("Masala")` calls would accumulate items in that same list. The active version creates a list inside the function and only prints it.

Lines starting with `#`, including the earlier string example and the mutable-default example, are comments and do not run.

Expected output:

```text
[1, 42, 3]
Darjeeling Yes Low
Green No Medium
Ingredients ('Cinnamon', 'Cardamom')
Extras {'sweetener': 'Honey', 'foam': 'yes'}
[]
[]
```

## Coding exercise 21: Order Invoice Generator

**Completed: Udemy tests passed.**

Read the [original challenge](CODING_EXERCISE_21.md) and the [Python solution](coding_exercise_21.py).

`generate_invoice()` returns one invoice string using three kinds of input:

| Parameter | Purpose |
| --- | --- |
| `customer_name: str = "Guest"` | The customer name, defaulting to `"Guest"` when omitted. |
| `*items: str` | Any number of food-item names, collected in a tuple. |
| `**charges: float` | Named extra charges, collected in a dictionary. |

The `-> str` annotation describes the returned value. The function builds the invoice in these steps:

1. Start a `lines` list with `Invoice for <customer_name>:`.
2. If items are present, append `Items:` and a separate `- <item>` line for each item.
3. If charges are present, append `Charges:` and iterate through `charges.items()`. `.capitalize()` turns a name such as `tax` into `Tax`.
4. Calculate `sum(charges.values(), 0.0)`, then append the total line. Only charge amounts contribute to the total; food items are listed by name.
5. Return `"\n".join(lines)` to combine the list into one string with a newline between its entries.

After loading the function, this call:

```python
print(generate_invoice("Amit", "Burger", "Fries", tax=50.0, service=20.0))
```

displays:

```text
Invoice for Amit:
Items:
- Burger
- Fries
Charges:
Tax: 50.0
Service: 20.0
Total Amount Due: 70.0
```

Calling the function without arguments:

```python
print(generate_invoice())
```

displays:

```text
Invoice for Guest:
Total Amount Due: 0.0
```

Empty item and charge sections are omitted. The starting value `0.0` in `sum()` keeps the total at `0.0` when there are no charges. The function returns the text; the example caller uses `print()` to display it.

## Example 10: Return Values and Early Returns

Read [10_return.py](10_return.py). The active code demonstrates several return behaviours:

- `idle_chaiwala()` contains `pass`, a placeholder that does nothing. Reaching the end without an explicit `return` returns `None`, which the caller prints.
- `sold_cups()` returns `120`. The caller stores that value in `total`, then prints it.
- `chai_status(0)` returns `"Sorry, chai over"` immediately. With `5`, the function reaches the next return and gives `"Chai is ready"`.
- `return` ends the current function call. The `print("chai")` below the unconditional return is unreachable and never runs.
- `chai_report()` returns `100, 20, 10` as one tuple. `sold, remaining, not_paid = chai_report()` unpacks its values into three variables. The script prints `sold` and `remaining`; `not_paid` receives `10`.

The earlier `make_chai()` example is commented out and does not run.

Expected output:

```text
None
120
Sorry, chai over
Chai is ready
Sold:  100
Remaining:  20
```

## Example 11: Function Behaviour, Recursion, and Filtering

Read [11_types_of_functions.py](11_types_of_functions.py).

| Function | Behaviour |
| --- | --- |
| `pure_chai(cups)` | Returns `cups * 10` using its input, without changing external state. For example, `pure_chai(3)` returns `30`. |
| `impure_chai(cups)` | Adds `cups` to the global `total_chai`. Changing state outside the function is a side effect. |
| `pour_chai(n)` | Prints the current number and calls itself with `n - 1` until it reaches `0`. |

The script defines `pure_chai()` and `impure_chai()` without calling them, so they produce no output and `total_chai` stays at `0`.

Calling `pour_chai(3)` starts **recursion**, where a function calls itself. The calls proceed from `3` to `2`, `1`, and `0`. Each call prints its number before checking the stopping condition. At `0`, the function returns `"All cups poured"`. Each earlier call returns that same result, which the outer `print(pour_chai(3))` displays once.

The final example filters a list:

```python
chai_types = ["light", "kadak", "ginger", "kadak"]
strong_chai = list(filter(lambda chai: chai != "kadak", chai_types))
```

`lambda chai: chai != "kadak"` is a short function returning whether a value differs from `"kadak"`. `filter()` keeps values for which this condition is true, and `list()` collects them into a list. Both occurrences of `"kadak"` are removed, leaving `"light"` and `"ginger"`.

Expected output:

```text
3
2
1
0
All cups poured
['light', 'ginger']
```

## Coding exercise 22: Function Types

**Completed: Udemy tests passed.**

Read the [original challenge](CODING_EXERCISE_22.md) and the [Python solution](coding_exercise_22.py).

The solution contains four functions:

| Function | Behaviour |
| --- | --- |
| `pure_add(a, b)` | Returns the sum of its two arguments without relying on or changing external state. |
| `impure_increment()` | Adds `1` to the global `counter` and returns its new value. The counter starts at `0` and accumulates across calls. |
| `factorial_recursive(n)` | Returns the factorial of a nonnegative integer using recursive calls. The base case is `n == 0`, which returns `1`. |
| `square_list(nums)` | Returns a new list of squares using a lambda inside `map()`. The input list stays unchanged. |

For `factorial_recursive(5)`, each call multiplies its number by the result of the next call. Reaching `0` stops the recursion and returns `1`; the completed calculation gives `5 * 4 * 3 * 2 * 1 = 120`.

In `square_list()`, `map(lambda number: number**2, nums)` applies the squaring function to every element. `list()` collects those results into a new list. An empty input returns an empty list.

Starting with a fresh counter of `0`, these calls after loading the functions:

```python
print(pure_add(3, 5))
print(impure_increment())
print(impure_increment())
print(factorial_recursive(5))
print(square_list([1, 2, 3, 4]))
```

display:

```text
8
1
2
120
[1, 4, 9, 16]
```

`impure_increment()` uses the counter's current state, so successive calls return different values. `pure_add()` calculates its result entirely from its arguments.

## Example 12: Docstrings and Built-in Help

Read [12_built_in.py](12_built_in.py). A **docstring** is a string placed at the beginning of a function body to describe its purpose.

- `chai_flavor.__doc__` reads the function's docstring, `Return the flavor of chai.`
- `chai_flavor.__name__` reads its name, `chai_flavor`.
- `help(len)` displays documentation for the built-in `len()` function, which returns the number of items in an object such as a list or string.

The script first prints:

```text
Return the flavor of chai.
chai_flavor
```

This is followed by the help text for `len()`. Its exact presentation can vary with the Python version and terminal. Reading the function metadata does not call `chai_flavor()`.

The file also defines `generate_bill(chai=0, samosa=0)`. Its docstring describes the parameters and returned value. The calculation charges 10 rupees per chai and 15 per samosa, then returns a tuple containing the total and a thank-you message.

After loading the function, this example call:

```python
print(generate_bill(chai=2, samosa=3))
```

displays:

```text
(65, 'Thank you for visiting chaicode.com')
```

The script defines `generate_bill()` without calling it, so this bill appears only when a caller requests it.

## How to run these examples

Open the repository root in VS Code, select your Python interpreter, and open an example. Press **Ctrl + S** to format and run it using the project's editor settings.

Alternatively, run the examples from the repository root:

```powershell
python 05_functions/01_duplication.py
python 05_functions/02_complex.py
python 05_functions/03_hiding.py
python 05_functions/04_readability.py
python 05_functions/05_trace.py
python 05_functions/06_scopes.py
python 05_functions/07_nonlocal.py
python 05_functions/08_global_scope.py
python 05_functions/09_input_params.py
python 05_functions/10_return.py
python 05_functions/11_types_of_functions.py
python 05_functions/12_built_in.py
```

All twelve numbered scripts include function calls outside their definitions, so running them displays the output described above. A function definition alone does not run its body.

Exercises 19–22 define functions for automatic testing. Running these files alone does not display a result. The caller supplies the arguments and uses the returned values, as shown in the exercise examples above. `process_transactions()` updates global `loyalty_points`, and `impure_increment()` updates global `counter`.

See the [main README](../README.md#quick-start) for editor setup.
