OPERATORS = ["+", "-", "*", "/", "//", "%", "**"]

def read_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("That is not a valid number, try again.")

first = read_number("Enter the first number: ")

operator = input("Enter an operator (+, -, *, /, //, %, **): ").strip()
while operator not in OPERATORS:
    operator = input("Invalid operator. Choose from + - * / // % **: ").strip()

second = read_number("Enter the second number: ")

try:
    if operator == "+":
        result = first + second
    elif operator == "-":
        result = first - second
    elif operator == "*":
        result = first * second
    elif operator == "/":
        result = first / second
    elif operator == "//":
        result = first // second
    elif operator == "%":
        result = first % second
    else:
        result = first ** second
except ZeroDivisionError:
    print("Error: division by zero is not allowed.")
except OverflowError:
    print("Error: the result is too large to calculate.")
else:
    print(f"{first} {operator} {second} = {result}")