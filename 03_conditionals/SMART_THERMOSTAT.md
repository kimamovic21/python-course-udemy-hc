# Mini Project 4: Smart Thermostat

See the [Python example](smart_thermostat.py) and the [section learning order](README.md#learning-order).

## Problem statement

You are building a status checker for a smart thermostat. First, check whether the device is active. For an active device, inspect the temperature and display either a high-temperature alert or a normal-temperature message. For any other device status, display an offline message.

The starting values are:

```python
device_status = "active"
temperature = 38
```

## Tasks

1. Create the `device_status` and `temperature` variables using the starting values above.
2. Check whether `device_status` equals `"active"`.
3. Inside that condition, check whether `temperature` is greater than `35`.
4. Print the message matching the device status and temperature:

   | Device status | Temperature | Message |
   | --- | --- | --- |
   | `"active"` | Greater than `35` | `High temperature alert!` |
   | `"active"` | `35` or less | `Temperature is normal` |
   | Any other status | Any value | `Device is offline` |

## How the solution works

The program uses a **nested `if` statement**: an `if` inside another `if`.

```python
if device_status == "active":
    if temperature > 35:
        print("High temperature alert!")
    else:
        print("Temperature is normal")
else:
    print("Device is offline")
```

The outer `if` checks the device status. When it is `"active"`, execution enters that block and reaches the inner temperature check.

The inner `if` checks `temperature > 35`. Its `else` handles temperatures of `35` or less. The condition uses `>`, so exactly `35` is treated as normal.

The outer `else` handles every status other than `"active"`. In that branch, the program prints the offline message and skips the temperature check.

**Indentation shows which statements belong together.** Each `else` lines up with its matching `if`. This example uses four spaces per level, so the temperature messages are indented eight spaces inside the two nested blocks.

## Expected output

With `device_status = "active"` and `temperature = 38`:

```text
High temperature alert!
```

The device is active, and `38 > 35` is true. Exactly one message is printed.

## Try other values

Change the variables at the top of the Python file and run it again:

| `device_status` | `temperature` | Expected output |
| --- | --- | --- |
| `"active"` | `35` | `Temperature is normal` |
| `"active"` | `36` | `High temperature alert!` |
| `"inactive"` | `38` | `Device is offline` |

## How to run

From the repository root:

```powershell
python 03_conditionals/smart_thermostat.py
```

In VS Code, you can also open the Python file and press **Ctrl + S** to run it using the project's editor settings.
