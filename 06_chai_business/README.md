# 06 — Chai Business: Modules and Packages

This section introduces organising Python code into modules and packages. A small chai example shows how `main.py` can import and call functions defined in another file.

**Status: in progress.** The current example covers two import styles and two recipe functions. More lessons will be added as I continue the course.

## Learning order

1. Read [recipes/flavors.py](recipes/flavors.py) to see the functions and the strings they return.
2. Look at [recipes/__init__.py](recipes/__init__.py), the empty file marking `recipes` as a regular Python package.
3. Run [main.py](main.py) to compare importing a module with importing individual functions.

Follow this order even if your editor sorts the files differently.

## Files covered so far

```text
06_chai_business/
├── main.py
├── recipes/
│   ├── __init__.py
│   └── flavors.py
└── utils/
    └── discounts.py
```

| File | Purpose |
| --- | --- |
| [main.py](main.py) | Imports recipe functions in two ways and prints their returned messages. |
| [recipes/__init__.py](recipes/__init__.py) | Marks `recipes` as a regular package. Its code runs when the package is first imported; it is currently empty. |
| [recipes/flavors.py](recipes/flavors.py) | Defines `elaichi_chai()` and `ginger_chai()`. |
| [utils/discounts.py](utils/discounts.py) | An empty placeholder module. |

## Modules and Packages

A **module** is a Python file containing code that can be imported. Here, `flavors.py` is a module inside the `recipes` package.

A **package** groups related modules. The dotted name `recipes.flavors` identifies the `flavors` module within `recipes`.

The recipe functions return strings:

```python
def elaichi_chai():
    return "Elaichi chai is ready"


def ginger_chai():
    return "Ginger chai is ready"
```

Their callers use `print()` to display those returned messages.

## Importing a Module

The first part of `main.py` uses:

```python
import recipes.flavors

print(recipes.flavors.ginger_chai())
```

This imports the module. The function is accessed through its full name, `recipes.flavors.ginger_chai()`.

## Importing Individual Functions

The second part uses:

```python
from recipes.flavors import elaichi_chai, ginger_chai

print(ginger_chai())
print(elaichi_chai())
```

This makes the two function names available directly in `main.py`. Both import styles use the same functions. The example calls `ginger_chai()` twice in total to demonstrate each style.

Expected output from the complete `main.py`:

```text
Ginger chai is ready
Ginger chai is ready
Elaichi chai is ready
```

## How to Run

From the repository root:

```powershell
python 06_chai_business/main.py
```

Alternatively, select your interpreter in VS Code, open `main.py`, and press **Ctrl + S** to format and run it with the project's editor settings.

The recipe files are local to this example. See the [main README](../README.md#quick-start) for editor setup.

## Generated Cache Files

Importing the package and module can create `recipes/__pycache__/`. Its `.pyc` files contain compiled Python bytecode, which Python can reuse on later imports. The cache may include files for both `__init__.py` and `flavors.py`.

Python manages these binary files automatically and recreates them when needed. Read and edit the original `.py` files.

To exclude this generated cache from Git, the following patterns can be placed in the repository's `.gitignore`:

```gitignore
__pycache__/
*.pyc
```

Keep the source files and README in commits, and leave generated cache files out.
