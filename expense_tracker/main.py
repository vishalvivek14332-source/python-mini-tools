from datetime import datetime
from database import load_expenses, save_expenses

def add_expense():
    desc = input("Description: ")
    amount = float(input("Amount: "))
    category = input("Category: ")

    expenses = load_expenses()
    expenses.append({
        "date": datetime.now().strftime("%Y-%m-%d"),
        "description": desc,
        "amount": amount,
        "category": category,
    })
    save_expenses(expenses)
    print("Expense added!")

def list_expenses():
    for e in load_expenses():
        print(
            f"{e['date']} | {e['category']:<12} | "
            f"₹{e['amount']:.2f} | {e['description']}"
        )

def summary():
    total = sum(e["amount"] for e in load_expenses())
    print(f"Total spent: ₹{total:.2f}")

while True:
    print("\n1. Add\n2. List\n3. Summary\n4. Exit")
    choice = input("Choose: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        list_expenses()
    elif choice == "3":
        summary()
    elif choice == "4":
        break
    else:
        print("Invalid choice.")