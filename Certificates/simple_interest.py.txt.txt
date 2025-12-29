principal = float(input("Enter principal amount: "))
rate = float(input("Enter annual rate (e.g. 5 for 5%): "))
time = float(input("Enter time in years: "))

interest = principal * rate / 100 * time
print(f"Simple Interest: {interest}")
