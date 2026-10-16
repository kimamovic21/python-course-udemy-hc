# 02 — Data Types

This section explores Python values, objects, numbers, strings, and boolean logic through small examples about making tea and deciding whether to go for a walk.

**Status: in progress.** This checkpoint covers chapters 1–6 and two coding exercises: **Playing with Numbers** and **Should You Go for a Walk?** More lessons will be added as I continue the course.

## Files covered so far

| File | What it demonstrates |
| --- | --- |
| [chapter_1.py](chapter_1.py) | Integer values, variable reassignment, and object identity with `id()`. |
| [chapter_2.py](chapter_2.py) | Creating and changing a set with `set()` and `.add()`. |
| [chapter_3.py](chapter_3.py) | Arithmetic operators and readable large numbers. |
| [chapter_4.py](chapter_4.py) | Booleans, conversion with `bool()`, and the `and` operator. |
| [chapter_5.py](chapter_5.py) | Floating-point numbers, precision, and `sys.float_info`. |
| [chapter_6.py](chapter_6.py) | Strings, f-strings, slicing, reversing text, and UTF-8 encoding and decoding. |

## Coding exercise files

Each exercise has a Markdown file containing the original challenge and a separate Python file containing the solution. Read the challenge first, then compare it with the solution.

| Exercise | Challenge description | Python solution |
| --- | --- | --- |
| 01 — Playing with Numbers | [CODING_EXERCISE_01.md](CODING_EXERCISE_01.md) | [coding_exercise_01.py](coding_exercise_01.py) |
| 02 — Should You Go for a Walk? | [CODING_EXERCISE_02.md](CODING_EXERCISE_02.md) | [coding_exercise_02.py](coding_exercise_02.py) |

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

## Chapter 6: strings, slicing, and UTF-8

A **string** (`str`) stores text. `chai_type`, `customer_name`, `chai_description`, and `label_text` all contain strings in this example.

An **f-string** starts with `f` before the quotation marks. Expressions inside `{}` are replaced with their values, allowing the order message to include the customer's name and type of chai.

String slicing extracts part of a string or changes the direction in which it is read. For `chai_description = "Aromatic and Bold"`:

| Expression | Result | Explanation |
| --- | --- | --- |
| `chai_description[:8]` | `"Aromatic"` | Characters from the start up to, but not including, index `8`. |
| `chai_description[12:]` | `" Bold"` | Characters from index `12` to the end, including the space before `Bold`. |
| `chai_description[::-1]` | `"dloB dna citamorA"` | The entire description in reverse order. |

String indexes start at `0`. The reverse slice produces the whole reversed description, even though the current program labels that output as `Last word`.

The final part of the lesson converts `"Chai Spécial"` between text and bytes:

- `.encode("utf-8")` converts the string into a `bytes` object stored in `encoded_label`.
- The encoded value is displayed as `b'Chai Sp\xc3\xa9cial'`. The `b` prefix identifies bytes; the accented `é` is represented by two bytes in UTF-8.
- `.decode("utf-8")` converts those bytes back into the original string, stored in `decoded_label`.

Encoding and decoding with the same encoding restores the text, including its accented character.

## Coding exercise 01: Playing with Numbers

**Completed: all Udemy tests passed.**

Read the [challenge description](CODING_EXERCISE_01.md) and the [Python solution](coding_exercise_01.py).

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

## Coding exercise 02: Should You Go for a Walk?

Read the [challenge description](CODING_EXERCISE_02.md) and the [Python solution](coding_exercise_02.py).

The starting conditions are `is_sunny = True` and `have_umbrella = False`. The exercise combines these boolean values with three logical operators:

- `not` reverses a boolean value: `True` becomes `False`, and `False` becomes `True`.
- `and` returns `True` when both boolean conditions are `True`.
- `or` returns `True` when at least one boolean condition is `True`.

| Expression | Evaluation | Result |
| --- | --- | --- |
| `not is_sunny` | `not True` | `False` |
| `not have_umbrella` | `not False` | `True` |
| `is_sunny and not have_umbrella` | `True and True` | `True` |
| `is_sunny or have_umbrella` | `True or False` | `True` |

Expected output, in the order requested by the challenge:

```text
False
True
True
True
```

The solution prints only these four boolean values, one per line, without extra labels.

## How to run these examples

1. Open the repository root in VS Code and select your Python interpreter with **Python: Select Interpreter**.
2. Open the Python file you want to practise with.
3. Edit the file and press **Ctrl + S**. Black formats the code, then Run on Save runs it in the terminal.

To run a file manually, use **Python: Run Python File in Terminal** from the Command Palette (**Ctrl + Shift + P**). To format without saving, use **Shift + Alt + F**.

The [main README](../README.md#quick-start) lists the required extensions. Each file is a separate example and can be run independently.
