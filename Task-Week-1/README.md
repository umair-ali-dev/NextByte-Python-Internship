# Week 1 — Python Setup & Basics

This week I set up Python and VS Code and practiced variables, input/output,
operators and if/else. Python version: 3.14.6


## Programs
- greeting_program.py — ...
- calculator.py — ...
- grade_checker.py — ...
- type_demo.py — ...


## How to run
python Task-Week-1/greeting_program.py
python Task-Week-1/calculator.py
python Task-Week-1/grade_checker.py
python Task-Week-1/type_demo.py


## Program Output
## python Task-Week-1/greeting_program.py
Hi there! Let's get to know each other.
What is your name? Umair
How old are you? 22

Nice to meet you, Umair!
You are in your prime, keep building things.
You will turn 50 in 28 years (around 2054).

## python Task-Week-1/calculator.py
Enter the first number: 4
Enter an operator (+, -, *, /, //, %, **): *
Enter the second number: 5
4 * 5 = 20

## python Task-Week-1/grade_checker.py
Enter your marks (0-100): 78
Marks: 78 | Grade: B+
Result: Pass

## python Task-Week-1/type_demo.py
Basic types
age = 22 -> int
price = 49.95 -> float
name = 'Anas' -> str
is_student = True -> bool
nothing = None -> NoneType

Conversions
int("42") -> 42 (int)
float("3.5") -> 3.5 (float)
str(100) -> '100' (str)
int(7.9) -> 7 (int)
float(5) -> 5.0 (float)
bool(0) -> False (bool)
bool("") -> False (bool)
bool("text") -> True (bool)

Operators
7 + 2 = 9
7 / 2 = 3.5
7 // 2 = 3
7 % 2 = 1
7 ** 2 = 49
7 > 2 and 2 < 5 -> True


## What I learned / problems I hit
This week I got comfortable with taking user input, converting types with int() and float(), and using if/elif/else to make decisions. The biggest lesson was that input()always returns a string, so I had to convert it and handle bad input with try/except inside a while loop instead of letting the program crash.