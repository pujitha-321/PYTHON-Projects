#This is the code to calculate Compound Interest of a give amount
principal = 0
rate = 0
time = 0
n = 0

while True:
    principal = float(input("Enter the principal amount: "))
    if principal <= 0:
        print("Principal amount cannot be zero or negative.")
    else:
        break

while True:
    rate = float(input("Enter the annual interest rate (%): "))
    if rate <= 0:
        print("Rate cannot be zero or negative.")
    else:
        break

while True:
    time = int(input("Enter the time (in years): "))
    if time <= 0:
        print("Time cannot be zero or negative.")
    else:
        break

while True:
    n = int(input("Enter the number of times interest is compounded per year: "))
    if n <= 0:
        print("Value cannot be zero or negative.")
    else:
        break

amount = principal * (1 + (rate / 100) / n) ** (n * time)
compound_interest = amount - principal

print("\n----- Compound Interest Calculator -----")
print("Principal Amount :", principal)
print("Rate             :", rate, "%")
print("Time             :", time, "years")
print("Compounded       :", n, "times/year")
print("Compound Interest:", round(compound_interest, 2))
print("Final Amount     :", round(amount, 2))
