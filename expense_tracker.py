print("Welcome to Smart Expense Tracker")
import os
print("Current working directory:", os.getcwd())
import csv
import os

FILE_NAME = "expenses.csv"

# Create file with header if it does not exist
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Category", "Amount"])

while True:
    print("\n--- Smart Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        date = input("Enter date (YYYY-MM-DD): ")
        category = input("Enter category (Food/Travel/etc): ")
        amount = float(input("Enter amount: "))

        with open(FILE_NAME, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([date, category, amount])

        print("✅ Expense saved successfully!")

    elif choice == "2":
        print("\n📋 All Expenses:\n")
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)

    elif choice == "3":
        print("👋 Exiting... Thank you!")
        break

    else:
        print("❌ Invalid choice. Try again.")
