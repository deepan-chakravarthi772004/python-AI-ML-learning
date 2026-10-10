import json

try:
    with open("expenses.json","r") as file:
        expenses = json.load(file)
except FileNotFoundError:
    expenses = []

while True:
    print("\n=====EXPENSE TRACKER=====")
    print("1:Add Expenses")
    print("2:View Expenses")
    print("3:Total Expense")
    print("4:Exit")

    choice = input("enter your choice:")

    if choice == "1":
        name = input("Enter expense name:")
        try:
            amount = float(input("amount:"))

            if amount <= 0:
                print("Amount must greater than zero")
                continue

        except ValueError:
            print("please enter a valid amount")
            continue

        expenses.append({
            "name" : name,
            "amount" : amount
        })

        with open("expenses.json","w") as file:
            json.dump(expenses,file,indent=4)

        print("Expense added successfully")

    elif choice == "2":
        print("\nYour expenses:")

        if not expenses:
            print("not any expenses.")

        for expense in expenses:
            print(f"{expense['name']} - $ {expense['amount']}")

    elif choice == "3":
        total = sum(expense["amount"]for expense in expenses)

        print(f"Total expense: {total}$")

    elif choice == "4":
        print("Thank you for using Expense Tracker")
        break

    else:
        print("Invalid choice,Try Again")