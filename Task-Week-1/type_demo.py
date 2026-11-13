age = 22
price = 49.95
name = "Anas"
is_student = True
nothing = None

values = [
    ("age", age),
    ("price", price),
    ("name", name),
    ("is_student", is_student),
    ("nothing", nothing),
]

print("Basic types")
for label, value in values:
    print(f"{label} = {value!r} -> {type(value).__name__}")

conversions = [
    ('int("42")', int("42")),
    ('float("3.5")', float("3.5")),
    ("str(100)", str(100)),
    ("int(7.9)", int(7.9)),
    ("float(5)", float(5)),
    ("bool(0)", bool(0)),
    ('bool("")', bool("")),
    ('bool("text")', bool("text")),
]

print("\nConversions")
for expression, result in conversions:
    print(f"{expression} -> {result!r} ({type(result).__name__})")

print("\nOperators")
print("7 + 2 =", 7 + 2)
print("7 / 2 =", 7 / 2)
print("7 // 2 =", 7 // 2)
print("7 % 2 =", 7 % 2)
print("7 ** 2 =", 7 ** 2)
print("7 > 2 and 2 < 5 ->", 7 > 2 and 2 < 5)