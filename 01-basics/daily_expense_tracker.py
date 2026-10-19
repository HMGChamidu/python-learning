from pathlib import Path

DATA_FILE = Path("expenses.txt")


def add_expense():
    name = input("Expense name: ").strip()
    category = input("Category (Food/Transport/Bills/Other): ").strip()

    if not name or not category:
        print("Expense name and category cannot be empty.")
        return

    try:
        amount = float(input("Amount (LKR): ").strip())
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    with DATA_FILE.open("a", encoding="utf-8") as file:
        file.write(f"{name},{category},{amount:.2f}\\n")

    print("Expense saved successfully.")


def view_expenses():
    if not DATA_FILE.exists():
        print("No records found. Please add an expense first.")
        return

    records_found = False
    print("\\n--- ALL EXPENSES ---")
    with DATA_FILE.open("r", encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) != 3:
                continue
            name, category, amount = parts
            print(f"Name: {name} | Category: {category} | Amount: LKR {float(amount):,.2f}")
            records_found = True

    if not records_found:
        print("No records found. Please add an expense first.")


def calculate_total():
    if not DATA_FILE.exists():
        print("No records found. Please add an expense first.")
        return

    total = 0.0
    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    total += float(parts[2])
        print(f"Total Spent: LKR {total:,.2f}")
    except ValueError:
        print("A saved record contains an invalid amount.")


def main():
    while True:
        print("\\n===== DAILY EXPENSE TRACKER =====")
        print("1. Add New Expense")
        print("2. View All Expenses")
        print("3. Calculate Total Money Spent")
        print("4. Exit Program")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            calculate_total()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
