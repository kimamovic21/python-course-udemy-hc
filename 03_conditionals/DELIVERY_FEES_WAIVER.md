# Mini Project 5: Delivery Fees Waiver

See the [Python example](delivery_fees_waiver.py) and the [section learning order](README.md#learning-order).

## Problem statement

An online shop offers free delivery for orders greater than `300`. For orders of `300` or less, the delivery fee is `30`. Ask the customer for their order amount, choose the correct delivery fee, and display it.

| Order amount | Delivery fee |
| --- | --- |
| Greater than `300` | `0` |
| `300` or less | `30` |

## Tasks

1. Ask for the order amount with `input()`.
2. Convert the entered text to an integer with `int()` and store it in `order_amount`.
3. Use a conditional expression to assign the appropriate value to `delivery_fees`.
4. Print the delivery fee using an f-string.

## How the solution works

The first line reads a whole-number order amount:

```python
order_amount = int(input("Enter the order amount: "))
```

`input()` returns text. `int()` converts that text into a whole number so it can be compared with `300`.

The next line uses a **conditional expression**, also called a ternary expression:

```python
delivery_fees = 0 if order_amount > 300 else 30
```

Read it as: assign `0` when `order_amount > 300` is true; otherwise, assign `30`.

Its general form is `value_if_true if condition else value_if_false`. This expression selects a value to store in the variable. The equivalent longer form is:

```python
if order_amount > 300:
    delivery_fees = 0
else:
    delivery_fees = 30
```

Finally, the f-string inserts `delivery_fees` into the printed message.

## Example runs

An order that qualifies for free delivery:

```text
Enter the order amount: 450
Delivery fees is : 0
```

An order exactly at the threshold:

```text
Enter the order amount: 300
Delivery fees is : 30
```

The comparison uses `>`, so exactly `300` still has a delivery fee. Try `299`, `300`, and `301`: the fees should be `30`, `30`, and `0`, respectively.

## How to run

From the repository root:

```powershell
python 03_conditionals/delivery_fees_waiver.py
```

When prompted, enter a whole number and press **Enter**.
