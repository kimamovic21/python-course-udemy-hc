# 05 — Functions

This section introduces functions: named blocks of code that run when called. The examples cover parameters, code reuse, workflows built from smaller functions, and returned values used in bill and VAT calculations. Exercise 19 combines functions and conditions to generate student grade reports.

**Status: in progress.** This checkpoint covers five numbered examples and coding exercise 19. More lessons will be added as I continue the course.

## Learning order

1. Start with [01_duplication.py](01_duplication.py) to define a function with parameters and reuse it for three chai orders.
2. Continue with [02_complex.py](02_complex.py) to build a workflow by calling smaller functions in order.
3. Continue with [03_hiding.py](03_hiding.py) to group registration steps behind a single function call.
4. Continue with [04_readability.py](04_readability.py) to return a calculated bill and use the result in different ways.
5. Continue with [05_trace.py](05_trace.py) to reuse a VAT calculation in a loop and inspect each result.
6. Read the [original challenge 19](CODING_EXERCISE_19.md), then explore [coding_exercise_19.py](coding_exercise_19.py) to calculate a grade and return a student report.

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

## How to run these examples

Open the repository root in VS Code, select your Python interpreter, and open an example. Press **Ctrl + S** to format and run it using the project's editor settings.

Alternatively, run the examples from the repository root:

```powershell
python 05_functions/01_duplication.py
python 05_functions/02_complex.py
python 05_functions/03_hiding.py
python 05_functions/04_readability.py
python 05_functions/05_trace.py
```

All five scripts include function calls outside their definitions, so running them displays the output shown above. A function definition alone does not run its body.

`coding_exercise_19.py` defines functions for automatic testing. Running that file alone defines the functions without displaying a result. The caller supplies the arguments and uses the returned grade or report, as shown in the exercise example above.

See the [main README](../README.md#quick-start) for editor setup.
