# 03 — Conditionals

This section introduces `if` statements: running a block of code when a condition is true.

**Status: in progress.** This checkpoint covers one mini story and coding exercise 07. More examples will be added as I continue the course.

## Learning order

**Start with Mini story 1: Is the Kettle Ready?** It is the first mini project in `03_conditionals`. Follow the order below even if your editor sorts the files differently:

1. **Mini project 1:** Read [MINI_STORY.md](MINI_STORY.md), then work through [mini_story_1.py](mini_story_1.py).
2. **Coding exercise 07:** Read [CODING_EXERCISE_07.md](CODING_EXERCISE_07.md), then work through [coding_exercise_07.py](coding_exercise_07.py).

As more mini projects are added, their learning order and explanations will be documented here.

## Files covered so far

| File | Purpose |
| --- | --- |
| [MINI_STORY.md](MINI_STORY.md) | The kettle story, its tasks, and a change to try. |
| [mini_story_1.py](mini_story_1.py) | A boolean variable controlling a printed message with `if`. |
| [CODING_EXERCISE_07.md](CODING_EXERCISE_07.md) | The original Customer Discount Eligibility challenge, maintained manually. |
| [coding_exercise_07.py](coding_exercise_07.py) | Two independent `if` statements checking purchase amount and customer age. |

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

## How to run these examples

Open the repository root in VS Code, select your Python interpreter, and open the example you want to run. Press **Ctrl + S** to format and run it using the project's editor settings.

Alternatively, run these commands from the repository root:

```powershell
python 03_conditionals/mini_story_1.py
python 03_conditionals/coding_exercise_07.py
```

Each file runs independently and uses features included with Python. See the [main README](../README.md#quick-start) for editor setup.
