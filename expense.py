import csv
import os
from datetime import datetime
from collections import defaultdict

filename = "expenses.csv"

# Ensure file exists with headers
if not os.path.exists(filename):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Amount", "Category", "Date"])

# Add a new expense
def add_expense():
    try:
        amount = float(input("Enter amount (₹): "))
        category = input("Enter category (e.g. Food, Travel): ").capitalize()
        date_input = input("Enter date (YYYY-MM-DD) [Leave blank for today]: ")
        date = date_input if date_input else datetime.now().strftime("%Y-%m-%d")

        with open(filename, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([amount, category, date])
        print("✅ Expense added!")
    except ValueError:
        print("❌ Invalid amount entered.")

# View all expenses
def view_expenses():
    print("\n--- All Expenses ---")
    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                print(f"₹{row[0]} | {row[1]} | {row[2]}")
    except FileNotFoundError:
        print("❌ No expenses found.")

# Show total expenses
def total_expense():
    total = 0
    with open(filename, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            total += float(row[0])
    print(f"\n💰 Total Spent: ₹{total}")

# Show monthly total
def monthly_total():
    month = input("Enter month (MM): ")
    year = input("Enter year (YYYY): ")
    total = 0
    with open(filename, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if row[2].startswith(f"{year}-{month}"):
                total += float(row[0])
    print(f"📅 Total spent in {month}/{year}: ₹{total}")

# Show category-wise total
def category_total():
    category_data = defaultdict(float)
    with open(filename, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            category_data[row[1]] += float(row[0])
    
    print("\n📊 Expense by Category:")
    for cat, amt in category_data.items():
        print(f"{cat}: ₹{amt}")

# Main menu
while True:
    print("\n====== Personal Expense Tracker ======")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Show Total Expenses")
    print("4. Show Monthly Total")
    print("5. Show Expenses by Category")
    print("6. Exit")
    choice = input("Choose an option (1-6): ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_expense()
    elif choice == "4":
        monthly_total()
    elif choice == "5":
        category_total()
    elif choice == "6":
        print("👋 Exiting. Goodbye!")
        break
    else:
        print("❌ Invalid choice. Try again.")



