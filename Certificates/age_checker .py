age = int(input("How old are you? "))
if age < 0:
    print("Age cannot be negative.")
elif age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
