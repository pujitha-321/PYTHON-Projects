//Simple ATM SIMULATION SYSTEM
Balance = 5000

while True:
    print("\n1.Check Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Balance:", Balance)

    elif choice == 2:
        amount = int(input("Enter the deposited amount: "))
        Balance += amount
        print("The total Balance is:", Balance)

    elif choice == 3:
        withdraw_amount = int(input("Enter the withdraw amount: "))

        if Balance >= withdraw_amount:
            Balance -= withdraw_amount
            print("Your Balance is:", Balance)
            print("Amount withdrawn Successfully!")
        else:
            print("Insufficient Balance!")

    elif choice == 4:
        print("Exit the transaction")
        break

    else:
        print("Invalid choice")
