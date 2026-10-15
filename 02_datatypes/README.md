# 02 — Data Types

This section explores Python values, objects, and basic number operations through small examples about making tea.

**Status: in progress.** This checkpoint covers chapters 1–5 and the completed **Playing with Numbers** exercise. More lessons will be added as I continue the course.

## Files covered so far

| File | What it demonstrates |
| --- | --- |
| [chapter_1.py](chapter_1.py) | Integer values, variable reassignment, and object identity with `id()`. |
| [chapter_2.py](chapter_2.py) | Creating and changing a set with `set()` and `.add()`. |
| [chapter_3.py](chapter_3.py) | Arithmetic operators and readable large numbers. |
| [chapter_4.py](chapter_4.py) | Booleans, conversion with `bool()`, and the `and` operator. |
| [chapter_5.py](chapter_5.py) | Floating-point numbers, precision, and `sys.float_info`. |
| [coding_exercise_01.py](coding_exercise_01.py) | Playing with Numbers: six arithmetic operations with exact output. |

## Chapter 1: integers and object identity

`sugar_amount` first refers to the integer `2`, then is reassigned to `12`.

- An integer (`int`) represents a whole number.
- Integers are **immutable**: their value cannot be changed in place. Reassigning the variable makes it refer to another object.
- `id()` returns a number identifying an object during its lifetime. The calls to `id(2)` and `id(12)` inspect the identities of those two integer objects.

The sugar values printed are `2` and `12`. Object IDs can differ between program runs, so the exact ID numbers are not expected output to memorise.

## Chapter 2: mutable sets

`spice_mix = set()` creates an empty **set**. The program adds `"Ginger"`, `"cardamom"`, and `"lemon"` with `.add()`.

- A set stores unique values. Adding the same value again does not create a duplicate.
- A set does not guarantee the order in which its contents are displayed.
- Sets are **mutable**: `.add()` changes the existing object, so its ID stays the same before and after these additions.

In the output, the lines containing `id(spice_mix)` show the object's identity; the lines containing `spice_mix` show its contents.

## Chapter 3: arithmetic and large numbers

The examples practise calculations with tea, milk, and cardamom:

| Operator | Meaning | Example from the lesson | Result |
| --- | --- | --- | --- |
| `+` | Addition | `14 + 3` | `17` |
| `-` | Subtraction | `14 - 3` | `11` |
| `/` | Division | `7 / 4` | `1.75` |
| `//` | Floor division | `7 // 4` | `1` |
| `%` | Remainder | `10 % 3` | `1` |
| `**` | Exponentiation | `2 ** 3` | `8` |

Each calculation uses the variables in its expression. Calculating `total_grams` does not change `black_tea_grams`, which still contains `14` when the subtraction runs.

For these integer inputs, `/` returns a `float`, while `//` returns an `int` by rounding the quotient down. The `%` operator gives the remainder. `2 ** 3` means `2 * 2 * 2`.

The literal `1_000_000_000` is one billion. Underscores make the number easier to read without changing its value; the program prints it as `1000000000`.

## Chapter 4: booleans and conditions

A **boolean** (`bool`) has one of two values: `True` or `False`.

- In arithmetic, `True` acts as `1` and `False` as `0`. Therefore, `5 + True` produces `6`.
- `bool(0)` produces `False`, which represents the absence of milk in this example.
- With the two boolean values used here, `water_hot and tea_added` is `True` when both are `True`.

Expected output:

```text
Total actions: 6
Is there milk? False
Can we serve chai? True
```

## Chapter 5: floats and precision

`ideal_temp = 95.5` and `current_temp = 95.49` are **floating-point numbers** (`float`). The program prints both temperatures, subtracts them, and displays `sys.float_info`.

Many decimal values are stored approximately as binary floating-point numbers. As a result, the subtraction can display a value very close to `0.01` with extra decimal digits. This is normal floating-point behaviour.

`sys.float_info` describes the precision and range of Python's floating-point numbers. There is no need to memorise all of its fields at this stage.

`Fraction` and `Decimal` are also imported in the current file, but are not used in its calculations yet.

## Coding exercise 01: Playing with Numbers

**Completed: all Udemy tests passed.**

The program uses `first_number = 10` and `second_number = 5`. It prints the results of addition (`+`), subtraction (`-`), multiplication (`*`), division (`/`), floor division (`//`), and modulus (`%`), in that order.

Expected output:

```text
15
5
50
2.0
2
0
```

The exercise prints **only the results**, one per line. Labels such as `Addition:` or `Division:` made the Udemy tests fail because the tests expected an exact output match.

Notice that `/` produces `2.0`, a `float`, even though the division has no remainder. With these integer inputs, `//` produces `2`, an `int`.

## How to run these examples

1. Open the repository root in VS Code and select your Python interpreter with **Python: Select Interpreter**.
2. Open the Python file you want to practise with.
3. Edit the file and press **Ctrl + S**. Black formats the code, then Run on Save runs it in the terminal.

To run a file manually, use **Python: Run Python File in Terminal** from the Command Palette (**Ctrl + Shift + P**). To format without saving, use **Shift + Alt + F**.

The [main README](../README.md#quick-start) lists the required extensions. Each file is a separate example and can be run independently.
