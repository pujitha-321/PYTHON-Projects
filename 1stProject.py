TO CALCULATE STUDENT EXAM DETAILS
name = input("Enter your name: ")

sub1 = int(input("Enter sub1 marks: "))
sub2 = int(input("Enter sub2 marks: "))
sub3 = int(input("Enter sub3 msrks: "))
total = sub1 + sub2 + sub3
average = total/3
percentage = (total/300)*100

print(f"Student{name}")
print(f"percentage: {percentage:.2f}")
print(f"Total:{total:.2f}")
print(f"Average:{average:.2f}")

if percentage >= 35:
   print("PASS")
else:
   print("FAIL")
