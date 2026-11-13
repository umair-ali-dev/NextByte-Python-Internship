while True:
    try:
        marks = float(input("Enter your marks (0-100): "))
    except ValueError:
        print("Please enter a number.")
        continue
    if 0 <= marks <= 100:
        break
    print("Marks must be between 0 and 100.")

if marks >= 85:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 75:
    grade = "B+"
elif marks >= 70:
    grade = "B"
elif marks >= 65:
    grade = "C+"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "F"

print(f"Marks: {marks:g} | Grade: {grade}")

if grade == "F":
    print("Result: Fail")
else:
    print("Result: Pass")