"""
Infinite generator that simulates a token dispenser.

- Yields incrementing token numbers starting from `start`.
- Accepts input via `send()` to optionally reset the counter to a new value.
- Gracefully stops if `close()` is called.
"""


def token_dispenser(start: int = 1):
    token = start

    try:
        while True:
            reset_value = yield token
            if reset_value is not None:
                token = reset_value
            else:
                token += 1
    except GeneratorExit:
        print("Dispenser closed.")
