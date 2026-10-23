# 04 — Loops

This section introduces `for` loops and `range()` through small chai examples, then uses a loop to build a multiplication table.

**Status: in progress.** This checkpoint covers two numbered examples and coding exercise 13. More lessons will be added as I continue the course.

## Learning order

1. Start with [01_token_dispenser.py](01_token_dispenser.py) to repeat an action for tokens 1–10.
2. Continue with [02_batch_chai.py](02_batch_chai.py) to prepare four batches of chai.
3. Read the [original challenge 13](CODING_EXERCISE_13.md), then explore [coding_exercise_13.py](coding_exercise_13.py).

Follow this order even if your editor sorts the files differently. The two numbered examples are explained below.

## Files covered so far

| File | Purpose |
| --- | --- |
| [01_token_dispenser.py](01_token_dispenser.py) | A `for` loop printing a message for each token number. |
| [02_batch_chai.py](02_batch_chai.py) | A `for` loop printing a message for each batch. |
| [CODING_EXERCISE_13.md](CODING_EXERCISE_13.md) | The original Generate Multiplication Table challenge, maintained manually. |
| [coding_exercise_13.py](coding_exercise_13.py) | A function building and returning a list of multiplication-table strings. |

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

## How to run these examples

Open the repository root in VS Code, select your Python interpreter, and open an example. Press **Ctrl + S** to format and run it using the project's editor settings.

Alternatively, run the numbered examples from the repository root:

```powershell
python 04_loops/01_token_dispenser.py
python 04_loops/02_batch_chai.py
```

Exercise 13 defines a function for automatic testing. The tests call `multiplication_table(number)` and check the returned list. Running that file alone defines the function without displaying a result. A caller can use `print(multiplication_table(3))` to display the list.

See the [main README](../README.md#quick-start) for editor setup. These examples use features included with Python.
