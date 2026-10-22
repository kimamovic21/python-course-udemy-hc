# Snack Suggestion

You are serving tea and want to offer a snack. Cookies and samosa are available. Ask the customer what they prefer, then display a message based on their choice.

See the [Python example](snak_suggestion.py).

## Tasks

1. Ask for the customer's preferred snack with `input()` and store the answer in `snack`.
2. Convert the answer to lowercase with `.lower()`.
3. Use an `if` statement to check whether the answer is `"cookies"` or `"samosa"`.
4. If either option matches, print a confirmation containing the snack's name.
5. Otherwise, use `else` to explain which snacks are available.

## How the code works

| Code | Purpose |
| --- | --- |
| `input("Enter your preferred snack: ")` | Displays a prompt, waits for input, and returns the entered text as a string. |
| `.lower()` | Converts the text to lowercase, so `Cookies` and `COOKIES` both become `cookies`. |
| `snack == "cookies"` | Checks whether the entered value equals `"cookies"`. |
| `or` | Makes the condition true when at least one of the two snack comparisons is true. |
| `if` / `else` | Runs the confirmation block when the condition is true, or the alternative block when it is false. |
| `f"Great Choice! We'll serve you {snack}"` | Inserts the selected snack into the confirmation message. |

Both comparisons are written explicitly: `snack == "cookies" or snack == "samosa"`.

## Example runs

An available snack, entered with a capital letter:

```text
Enter your preferred snack: Cookies
Great Choice! We'll serve you cookies
```

A snack that is not available:

```text
Enter your preferred snack: chips
Sorry, we only serve cookies or samosa with tea
```

Try `samosa` and `SAMOSA` too. Both should produce the confirmation with `samosa` in lowercase.

## How to run

From the repository root:

```powershell
python 03_conditionals/snak_suggestion.py
```

When the prompt appears, type your snack in the terminal and press **Enter**.

See the [section README](README.md) for the earlier examples and learning order.
