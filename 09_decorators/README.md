# 09 — Decorators

This section introduces decorators: functions that receive another function and return a function used in its place. The examples add messages around calls, forward arguments, check a user role, and cache calculation results.

**Status: in progress.** This checkpoint covers three numbered examples and coding exercise 25.

**Review quiz: passed.** The quiz reviewed generators and decorator basics.

## Learning order

1. Start with [01_basics.py](01_basics.py) to wrap a function and preserve its metadata with `functools.wraps`.
2. Continue with [02_logging_decorator.py](02_logging_decorator.py) to forward arguments and return values while logging a call.
3. Continue with [03_auth_decorator.py](03_auth_decorator.py) to allow the wrapped function to run only for the `"admin"` role.
4. Read the [original challenge 25](CODING_EXERCISE_25.md), then explore [coding_exercise_25.py](coding_exercise_25.py) to cache multiplication results.

Follow this order even if your editor sorts the files differently. The numbered examples are explained below.

## Files covered so far

| File | Purpose |
| --- | --- |
| [01_basics.py](01_basics.py) | Printing messages before and after a function call, then inspecting the preserved function name. |
| [02_logging_decorator.py](02_logging_decorator.py) | Logging a function call, forwarding positional and keyword arguments, and returning its result. |
| [03_auth_decorator.py](03_auth_decorator.py) | Checking the supplied role before calling the original function. |
| [CODING_EXERCISE_25.md](CODING_EXERCISE_25.md) | The original Caching Expensive Calculations challenge, maintained manually. |
| [coding_exercise_25.py](coding_exercise_25.py) | A caching decorator applied to `multiply(a, b)`, returning messages for new and cached results. |

## Example 01: A Basic Decorator

Read [01_basics.py](01_basics.py). `my_decorator(func)` receives the original function and defines an inner `wrapper()` that:

1. Prints `Before function runs`.
2. Calls the original function through `func()`.
3. Prints `After function runs`.

`return wrapper` returns that function for later calls. Applying `@my_decorator` to `greet` corresponds to assigning `greet = my_decorator(greet)` after defining the original function.

Calling `greet()` therefore runs the wrapper, which calls the original greeting in the middle.

`@wraps(func)` preserves metadata such as the original name and docstring. This makes `greet.__name__` report `greet`; without it, the returned function's name would be `wrapper`.

Expected output:

```text
Before function runs
Hello from decorators class from chaicode
After function runs
greet
```

## Example 02: Logging and Forwarding Arguments

Read [02_logging_decorator.py](02_logging_decorator.py). `log_activity` prints the original function's name before calling it, saves its result, prints the finished message, and returns the saved result.

| Expression | Role |
| --- | --- |
| `def wrapper(*args, **kwargs)` | Collect positional arguments in the `args` tuple and keyword arguments in the `kwargs` dictionary. |
| `func(*args, **kwargs)` | Unpack those arguments and pass them to the original function. |
| `return result` | Pass the original function's returned value back to the caller. |

For `brew_chai("Masala")`, `args` is `("Masala",)` and `kwargs` is empty. The original function uses its default `milk="no"`. It prints a message and implicitly returns `None`.

Expected output:

```text
🚀 Calling: brew_chai
Brewing Masala chai and milk status no
✅ Finished: brew_chai
```

## Example 03: Checking a User Role

Read [03_auth_decorator.py](03_auth_decorator.py). `require_admin` checks the role passed to its wrapper before calling the original `access_tea_inventory()` function.

- For `"user"`, it prints the denied message and returns `None` immediately.
- For `"admin"`, it calls `func(user_role)` and returns the original function's result.

The wrapper's `user_role` value is passed positionally to the original function's `role` parameter. The parameter names can differ.

Expected output:

```text
Access denied: Admins only
Access granted to tea inventory
```

## Coding exercise 25: Caching Expensive Calculations

**Completed: Udemy tests passed.**

Read the [original challenge](CODING_EXERCISE_25.md) and the [Python solution](coding_exercise_25.py).

`cache_results(func)` creates a dictionary when the decorator is applied. Its wrapper keeps access to that dictionary across calls:

1. Build a key with `(args, tuple(sorted(kwargs.items())))`.
2. If the key is already present, return `From Cache: <result>` immediately.
3. Otherwise, call the original function with `func(*args, **kwargs)`.
4. Store its numeric result under that key and return `Computed: <result>`.

Sorting the keyword pairs makes keyword order irrelevant to the key. In this implementation, positional and keyword forms of a call use separate keys. Each decorated function has its own cache.

The dictionary stores the original result, while the wrapper returns a message containing it. Checking `key in cache` also recognises cached results of `0`.

After loading the exercise with a fresh cache, these calls:

```python
print(multiply(2, 3))
print(multiply(2, 3))
print(multiply(4, 5))
print(multiply(2, 3))
```

display:

```text
Computed: 6
From Cache: 6
Computed: 20
From Cache: 6
```

The repeated calls reuse their saved results, so the original multiplication is skipped on cache hits. `@wraps(func)` preserves the original function's metadata.

## How to run these examples

Open the repository root in VS Code, select your Python interpreter, and open a numbered example. Press **Ctrl + S** to format and run it using the project's editor settings.

Alternatively, run the numbered examples from the repository root:

```powershell
python 09_decorators/01_basics.py
python 09_decorators/02_logging_decorator.py
python 09_decorators/03_auth_decorator.py
```

All three numbered scripts include calls that produce the output shown above.

`coding_exercise_25.py` defines the decorator and decorated function for automatic testing. Running that file alone does not display a result. A caller invokes `multiply()` and can print its returned messages, as shown in the exercise example.

See the [main README](../README.md#quick-start) for editor setup.
