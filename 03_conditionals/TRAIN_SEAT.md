# Mini Project 6: Train Seat

See the [Python example](train_seat.py) and the [section learning order](README.md#learning-order).

## Problem statement

You are building a small helper for a train booking system. A passenger enters a seat type, and the program displays its description. The available options are sleeper, AC, general, and luxury. An unsupported choice should produce an invalid-seat message.

| Seat type | Printed description |
| --- | --- |
| `sleeper` | `Sleeper - No AC, beds available` |
| `ac` | `AC - Air conditioned, comfy ride` |
| `general` | `General - Cheapest option, no reservation` |
| `luxury` | `Luxury - Premium seats with meals` |
| Any other value | `Invalid seat type` |

## Tasks

1. Ask the passenger for a seat type using `input()`.
2. Convert the answer to lowercase with `.lower()` and store it in `seat_type`.
3. Use `match seat_type` and a `case` for each supported option.
4. Print the description for the matching seat type.
5. Add a final `case _` that prints `"Invalid seat type"` for other answers.

## How the solution works

The first line reads and normalises the answer:

```python
seat_type = input("Enter seat type (sleeper/AC/general/luxury)").lower()
```

`input()` waits for text entered in the terminal. `.lower()` converts that text to lowercase, so `AC`, `Ac`, and `ac` all become `ac`.

`match seat_type` then checks the value against the string patterns in the `case` branches. For example, the input `AC` becomes `ac` and matches `case "ac"`.

The first matching case runs, and the remaining cases are skipped. This example prints one description per run.

The final `case _` is a **wildcard**: it matches any remaining value. It provides the fallback message when the passenger enters an unsupported seat type. Keep it after the specific cases.

Indentation groups each `print()` with its corresponding `case` inside the `match` block.

## Example runs

Input: `AC`

```text
AC - Air conditioned, comfy ride
```

Input: `first`

```text
Invalid seat type
```

Try all four supported options, including mixed-case inputs such as `Sleeper` and `LUXURY`, to explore the branches.

## How to run

This example uses `match`/`case`, available in Python 3.10 and later.

From the repository root:

```powershell
python 03_conditionals/train_seat.py
```

When prompted, enter a seat type in the terminal and press **Enter**.
