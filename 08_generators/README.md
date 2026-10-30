# 08 — Generators

This section introduces generator functions: functions that produce values on demand using `yield`. The examples cover finite and infinite generators, independent generator state, sending values, delegation with `yield from`, and closing a generator.

**Status: in progress.** This checkpoint covers four numbered examples and coding exercise 24. More lessons will be added as I continue the course.

## Learning order

1. Start with [01_basics.py](01_basics.py) to produce values with `yield` and consume them with `for` and `next()`.
2. Continue with [02_infinite_generators.py](02_infinite_generators.py) to request a limited number of values from independent infinite generators.
3. Continue with [03_send_generators.py](03_send_generators.py) to pass orders into a paused generator with `.send()`.
4. Continue with [04_close_generator.py](04_close_generator.py) to combine generators with `yield from` and close an active generator.
5. Read the [original challenge 24](CODING_EXERCISE_24.md), then explore [coding_exercise_24.py](coding_exercise_24.py) to generate, reset, and stop token numbers.

Follow this order even if your editor sorts the files differently. The numbered examples are explained below.

## Files covered so far

| File | Purpose |
| --- | --- |
| [01_basics.py](01_basics.py) | Comparing a returned list with generator functions, then consuming values with a loop and `next()`. |
| [02_infinite_generators.py](02_infinite_generators.py) | Producing numbered refills with two generators that maintain separate counters. |
| [03_send_generators.py](03_send_generators.py) | Starting a generator and sending chai orders into it. |
| [04_close_generator.py](04_close_generator.py) | Delegating to other generators and handling generator closure. |
| [CODING_EXERCISE_24.md](CODING_EXERCISE_24.md) | The original Smart Token Dispenser challenge, maintained manually. |
| [coding_exercise_24.py](coding_exercise_24.py) | An infinite token generator supporting custom starts, resets, and graceful closure. |

## Example 01: Yield and Next

Read [01_basics.py](01_basics.py). Calling a generator function creates a generator object. Its body starts when a caller requests a value. Each `yield` supplies one value and pauses execution; the next request resumes after that pause.

The `for` loop consumes all three values from `serve_chai()`. The later `get_chai_gen()` example supplies three more values through three calls to `next(chai)`.

`get_chai_list()` is also defined in the file. Calling it would construct and return a complete list; the script leaves that function uncalled.

Expected output:

```text
Cup 1: Masala Chai
Cup 2: Ginger Chai
Cup 3: Elaichi Chai
Cup 1
Cup 2
Cup 3
```

The commented fourth `next(chai)` call would raise `StopIteration` because the generator has no more values. A `for` loop handles that signal automatically and ends its iteration.

## Example 02: Independent Infinite Generators

Read [02_infinite_generators.py](02_infinite_generators.py). `infinite_chai()` starts a local counter at `1` and uses `while True` to keep producing numbered messages.

Each `yield` pauses the loop. On the next request, `count += 1` runs before the next message is produced. `refill` and `user2` are separate generator objects, so each has its own counter starting at `1`.

The first loop requests five values; the second requests six. `_` is the conventional name for a loop variable whose value is unused. These bounded loops finish even though the generators can keep producing values.

Expected output:

```text
Refil #1
Refil #2
Refil #3
Refil #4
Refil #5
Refil #1
Refil #2
Refil #3
Refil #4
Refil #5
Refil #6
```

## Example 03: Sending Orders into a Generator

Read [03_send_generators.py](03_send_generators.py). `next(stall)` starts `chai_customer()`, prints the welcome message, and pauses at the first `order = yield`.

`stall.send("Masala Chai")` resumes the generator and makes the paused `yield` expression receive `"Masala Chai"`. That value is assigned to `order`. The loop prints the preparation message and pauses at the next `yield`.

The next `.send("Lemon Chai")` supplies the next order and repeats the process. Advancing to the first `yield` with `next()` prepares the generator to receive its first non-`None` value.

Expected output:

```text
Welcome ! What chai would you like ?
Preparing: Masala Chai
Preparing: Lemon Chai
```

## Example 04: Delegation and Closing

Read [04_close_generator.py](04_close_generator.py). `full_menu()` uses `yield from` to pass on all values from `local_chai()`, followed by all values from `imported_chai()`. A single loop can therefore consume the combined menu.

The second example creates `chai_stall()`. Its first `next()` yields `"Waiting for chai order"`, which the caller prints. `.close()` then raises `GeneratorExit` inside the paused generator. The example's exception handler catches it and prints the closing message.

Expected output:

```text
Masala Chai
Ginger Chai
Matcha
Oolong
Waiting for chai order
Stall closed, No more chai
```

## Coding exercise 24: Smart Token Dispenser

**Completed: Udemy tests passed.**

Read the [original challenge](CODING_EXERCISE_24.md) and the [Python solution](coding_exercise_24.py).

`token_dispenser(start: int = 1)` creates an infinite generator with its own local token counter.

| Operation | Behaviour |
| --- | --- |
| First `next(dispenser)` | Yields the starting token, which defaults to `1`. |
| Later `next(dispenser)` calls | Increment the counter and yield the next number. |
| `dispenser.send(value)` | Reset the counter to `value` and yield that number. |
| `dispenser.send(None)` | Continue normally, like `next(dispenser)`. |
| `dispenser.close()` | Close an active generator and print `Dispenser closed.`. |

`reset_value = yield token` both supplies the current token and receives a value when execution resumes. The `is not None` check allows a reset to `0`; an ordinary `next()` supplies `None` and takes the incrementing branch. `except GeneratorExit` handles closure explicitly.

After loading the function, this example:

```python
dispenser = token_dispenser()
print(next(dispenser))
print(next(dispenser))
print(dispenser.send(10))
print(next(dispenser))
dispenser.close()
```

displays:

```text
1
2
10
11
Dispenser closed.
```

Passing a different `start` changes the first number, and separate dispenser objects maintain independent counters.

## How to run these examples

Open the repository root in VS Code, select your Python interpreter, and open a numbered example. Press **Ctrl + S** to format and run it using the project's editor settings.

Alternatively, run the numbered examples from the repository root:

```powershell
python 08_generators/01_basics.py
python 08_generators/02_infinite_generators.py
python 08_generators/03_send_generators.py
python 08_generators/04_close_generator.py
```

All four numbered scripts include calls that produce the output shown above. The infinite-generator examples use a fixed number of requests or an explicit close so the scripts can finish.

`coding_exercise_24.py` defines a generator function for automatic testing. Running that file alone does not display a result. A caller creates the generator and uses `next()`, `.send()`, and `.close()`, as shown in the exercise example.

See the [main README](../README.md#quick-start) for editor setup.
