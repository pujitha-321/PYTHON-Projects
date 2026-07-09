#THESE ARE MY BASIC PYTHON PROJECTS WHICH I PRACTICE DAILY
num = 1
while num <= 5:
    print(num)
    j = 1
    while j<=3:
        print(j)
        j += 1
    num += 1
print()

#For LOOP
data = [3,'puji',4.6,'java']
for value in data:
    print(value)

#CONTINUE STATEMENT
for value in range(10):
    if value == 5:
        continue
    print(value)
print("Goodbye")

#BREAK STATEMENT
for value in range(10):
    if value == 6:
        break
    print(value)
print("byee bye")
