# 01 — Starter

This is the **first exercise folder** in my Python learning project. It introduces a first Python program, displaying text, and importing a module from Python's standard library.

## What is in main.py?

[`main.py`](main.py) currently contains:

```python
print("Hello, World!")

import this
```

Python runs these statements from top to bottom.

### 1. Display a greeting with print()

```python
print("Hello, World!")
```

- `print()` is a built-in Python function that displays a value in the terminal.
- `"Hello, World!"` is a **string**, which means a text value. The quotation marks mark where the text starts and ends.
- The parentheses contain the value passed to `print()`.

This line displays:

```text
Hello, World!
```

The quotation marks are part of the Python code and are not included in the displayed message.

### 2. Display The Zen of Python with import this

```python
import this
```

`import` loads a **module**, which is a file containing Python code that can be reused. Here, `this` is a module included in Python's standard library, so no additional installation is needed.

Importing `this` displays **The Zen of Python**, a collection of short principles about writing clear Python code. At this stage, just read through them; there is no need to memorise them.

The blank line between the two statements makes the code easier to read.

## How to run it

### First-time setup

1. Install **Python 3** from the [official Python website](https://www.python.org/).
2. Open the **root folder of this repository** in VS Code so that its `.vscode` settings are loaded.
3. Open Extensions with **Ctrl + Shift + X** and install:
   - [Python by Microsoft](https://marketplace.visualstudio.com/items?itemName=ms-python.python) — Python support and commands for running files.
   - [Run on Save by pucelle](https://marketplace.visualstudio.com/items?itemName=pucelle.run-on-save) — automatically runs the configured command when a Python file is saved.
4. Open `01_starter/main.py`. Press **Ctrl + Shift + P**, choose **Python: Select Interpreter**, and select your installed Python 3 interpreter.

### Run the program

1. Open the **root folder of this repository** in VS Code to load the project's editor settings.
2. Open `01_starter/main.py`.
3. Edit the code and press **Ctrl + S**. The configured Run on Save extension runs the file automatically in the terminal.

To run it manually, press **Ctrl + Shift + P** and choose **Python: Run Python File in Terminal**.

See the [main README](../README.md) for the project overview and links to the other exercise folders as they are added.

## Expected output

The program first displays `Hello, World!`, then The Zen of Python. The output begins with:

```text
Hello, World!
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
```

The remaining Zen of Python principles follow after these lines.

## Try it yourself

Change the greeting to your own message:

```python
print("Hello, Kerim!")
```

Save with **Ctrl + S** and check the new message in the terminal. Keep the text inside quotation marks and leave `import this` in place to see both parts of the program run again.
