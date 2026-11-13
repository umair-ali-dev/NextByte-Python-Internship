from datetime import date

HALF_CENTURY = 50
CENTURY = 100

print("Hi there! Let's get to know each other.")

name = str(input("What is your name? ")).strip()
while not name:
    name = input("Name cannot be empty. What is your name? ").strip()
name = name.title()

while True:
    try:
        age = int(input("How old are you? "))
    except ValueError:
        print("Please enter your age as a whole number.")
        continue
    if 1 <= age <= 120:
        break
    print("Age must be between 1 and 120.")

print(f"\nNice to meet you, {name}!")

if age < 12:
    print("You are still a kid, so enjoy it!")
elif age < 20:
    print("Teenage years, so much to learn ahead.")
elif age < HALF_CENTURY:
    print("You are in your prime, keep building things.")
else:
    print("So much experience, that is impressive.")

milestones = [HALF_CENTURY]
if age >= HALF_CENTURY:
    milestones.append(CENTURY)

current_year = date.today().year

for milestone in milestones:
    milestone_year = current_year - age + milestone
    years_difference = abs(milestone - age)
    unit = "year" if years_difference == 1 else "years"

    if age < milestone:
        print(f"You will turn {milestone} in {years_difference} {unit} (around {milestone_year}).")
    elif age == milestone:
        print(f"You are exactly {milestone} right now. Congratulations!")
    else:
        print(f"You turned {milestone} at {years_difference} {unit} ago (around {milestone_year}).")