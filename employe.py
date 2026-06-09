#THIS IS A SIMPLE CONDITIONAL PROGRAM PROGRAM USING LOGICAL AND OPERATOR
experience = int(input("Enter years of experience:"))
rating = int(input("Enter rating of employee:"))
if experience >=5 and rating >=5:
    print("Employee eligible for bonus")
else:
    print("Employee not eligible for bonus")
