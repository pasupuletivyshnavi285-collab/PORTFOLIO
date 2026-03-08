# Simple ATM Program

balance = 10000   # initial balance

while True:
    print("\n----- ATM Menu -----")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Your current balance is:", balance)

    elif choice == 2:
        amount = float(input("Enter amount to deposit: "))
        balance = balance + amount
        print("Amount deposited successfully.")
        print("Updated balance:", balance)

    elif choice == 3:
        amount = float(input("Enter amount to withdraw: "))
        if amount <= balance:
            balance = balance - amount
            print("Please collect your cash.")
            print("Remaining balance:", balance)
        else:
            print("Insufficient balance!")

    elif choice == 4:
        print("Thank you for using the ATM.")
        break

    else:
        print("Invalid choice! Please try again.")
