# Mini Project 3: Chai Price Calculator

See the [Python example](chai_price_calculator.py) and the [section learning order](README.md#learning-order).

## Problem statement

You run a chai shop that offers three cup sizes. Each size has a fixed price. Ask the customer which size they want, then display its price. If they enter an unsupported size, display a message explaining that the size is unknown.

| Cup size | Price |
| --- | --- |
| `small` | 10 rupees |
| `medium` | 15 rupees |
| `large` | 20 rupees |

## Tasks

1. Ask for a cup size with the prompt `Choose your cup size (small/medium/large): `.
2. Convert the answer to lowercase and store it in `cup`.
3. Use `if` to check for `"small"`.
4. Use `elif` branches to check for `"medium"` and `"large"`.
5. Print the matching price, or `"Unknown cup size"` if none of the sizes match.

## How the solution works

The first line reads the customer's answer:

```python
cup = input("Choose your cup size (small/medium/large): ").lower()
```

`input()` waits for the customer to type a value and press **Enter**. `.lower()` converts the text to lowercase, so `Medium`, `MEDIUM`, and `medium` all become `medium`.

The program then checks the conditions in order:

| Branch | Condition | Printed message |
| --- | --- | --- |
| `if` | `cup == "small"` | `Price is 10 rupees` |
| First `elif` | `cup == "medium"` | `Price is 15 rupees` |
| Second `elif` | `cup == "large"` | `price is 20 rupees` |
| `else` | None of the previous conditions matched. | `Unknown cup size` |

`elif` means **else if**: check another condition when the earlier conditions were false. Once a condition matches, its block runs and the remaining branches are skipped. The final `else` handles any other answer.

Only one message is printed per run. The program selects the fixed price associated with the requested cup size.

## Example runs

A supported size entered with a capital letter:

```text
Choose your cup size (small/medium/large): Medium
Price is 15 rupees
```

An unsupported size:

```text
Choose your cup size (small/medium/large): jumbo
Unknown cup size
```

## How to run

From the repository root:

```powershell
python 03_conditionals/chai_price_calculator.py
```

Enter a cup size in the terminal and press **Enter**. Try `small`, `MEDIUM`, `large`, and an unknown size to explore every branch.
