# QuickTools

A lightweight desktop app with six number and text utilities, built with Python and Tkinter. Pick a tool from the sidebar, enter a value, and get the result instantly. No external libraries required.

## Features

- Six tools in one clean, easy-to-navigate window
- Built-in example for every tool, shown on open and loaded with one click
- Input validation with clear error messages
- Reusable, loop-based functions kept separate from the interface code
- Modern layout with a sidebar, input card, and result panel

## Tools

| Tool | What it does | Example input | Example output |
|------|--------------|---------------|----------------|
| Factorial Calculator | Calculates the factorial of a whole number | `5` | `5! = 120` |
| Prime Finder | Lists every prime number in a range | `10`, `50` | `11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47` |
| Fibonacci Generator | Generates the Fibonacci sequence | `10` | `0, 1, 1, 2, 3, 5, 8, 13, 21, 34` |
| Palindrome Checker | Checks if text reads the same backwards, ignoring case, spaces and punctuation | `Never odd or even` | `Palindrome` |
| Digit Sum | Adds up all digits of a number | `4821` | `Digit sum of 4821 = 15` |
| Pyramid Generator | Prints a centred star pyramid | `4` | see below |

```
   *
  ***
 *****
*******
```

## Input Rules

| Tool | Field | Allowed values |
|------|-------|----------------|
| Factorial Calculator | Number | whole number, 0 to 100 |
| Prime Finder | From, To | whole numbers, 0 to 500 (`From` must not exceed `To`) |
| Fibonacci Generator | Terms | whole number, 1 to 50 |
| Palindrome Checker | Text | at least one letter or digit |
| Digit Sum | Number | whole number, 0 to 1,000,000,000,000 |
| Pyramid Generator | Rows | whole number, 1 to 12 |

Empty, non-numeric, and out-of-range entries show a message in red instead of a result.

## Requirements

- Python 3.10 or newer
- Tkinter (included with the standard Python installer on Windows and macOS)

On Debian or Ubuntu, install Tkinter with:

```bash
sudo apt install python3-tk
```

The interface uses the Segoe UI and Consolas fonts. On systems without them, Tkinter falls back to a default font automatically.

## Getting Started

```bash
git clone <repository-url>
cd <repository-folder>
python quicktools.py
```

## Usage

1. Choose a tool from the sidebar.
2. Enter your value, or click **Use example** to load the sample input.
3. Click **Calculate** or press **Enter**.

## Project Structure

The app is a single file, `quicktools.py`, organised in four parts:

| Part | Contents |
|------|----------|
| Logic functions | `factorial`, `is_prime`, `primes_in_range`, `fibonacci`, `is_palindrome`, `digit_sum`, `pyramid` |
| Validation | `Field` and `read_field`, which convert and check each entry |
| Tool registry | `Tool` and the `TOOLS` list that defines every tool in the app |
| Interface | `RoundedButton` and `App`, which build the window |

## Adding a New Tool

1. Write a function that returns the result as text.
2. Add a `Tool` entry to `TOOLS` with a name, description, input fields, the function, and an example.

```python
Tool(
    "Square Calculator",
    "Calculate the square of a whole number.",
    (Field("Number", maximum=1000),),
    lambda n: f"{n} squared = {n * n}",
    (12,),
),
```

The sidebar, input fields, validation, and example all update automatically.