import datetime

expenses = []
categories = ['Food', 'Transportation', 'Housing', 'Utilities', 'Entertainment', 'Other']
Currencies = ['USD','EUR','JPY','KRW','PHP']
# Exchange rates list, (Not Updated)
exchange_rates = {
    'USD': {'KRW': 1158.52, 'PHP': 50.32},
    'EUR': {'KRW': 1322.76, 'PHP': 57.49},
    'JPY': {'KRW': 10.56, 'PHP': 0.46},
    'KRW': {'USD': 0.00086, 'EUR': 0.00076, 'JPY': 0.094, 'PHP': 0.044},
    'PHP': {'USD': 0.020, 'EUR': 0.017, 'JPY': 2.16, 'KRW': 22.57},
}

# Define the budget dictionary
budgets = {category: 0 for category in categories}

# Function for initial login
def login_page():
    usernames = ["1", "2", "3"]
    passwords = ["1", "2", "3"]

    while True:
        # Verification process/loop
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        authenticated = False
        for i in range(3):
            if username == usernames[i] and password == passwords[i]:
                authenticated = True
                break

        if authenticated:
            print("\nLogin successful!")
            print("Logging in....\n")
            break
        else:
            print("\nWrong username or password. Please try again.\n")

# Function that adds category besides the original ones
def add_category():
    category = input("What category do you want to add? ")
    categories.append(category)
    print("\nThe category ",category, " is now added to the list of categories\n")

# Function to add an expense
def add_expense():
    main_currency = 'PHP'  # Define the main currency
    while True:
        date_str = input("Enter the date of the expense (dd/mm/yyyy): ")
        try:
            date = datetime.datetime.strptime(date_str, '%d/%m/%Y').date()
            break
        except ValueError:
            print("Invalid date format. Please enter the date in the format dd/mm/yyyy.")
    amount = float(input("Enter the amount of the expense: "))
    # Convert the amount to the user's main currency
    print("Currency:", Currencies)
    currency = input("Enter the currency of the expense: ")
    while currency not in exchange_rates:
        print("Invalid currency. Please choose from the following currencies:", ", ".join(exchange_rates.keys()))
        currency = input("Enter the currency of the expense: ")
    if currency != 'PHP':
        converted_amount =  exchange_rates[currency][main_currency]
        main_currency_amount = amount * converted_amount
        print("The converted value to PHP is : %.2f\n" % main_currency_amount)

    else:
        main_currency_amount = amount
    print("Categories:", categories)
    category = input("Enter the category of the expense: ")
    while category not in categories:
        print("Invalid category. Please choose from the following categories:", categories)
        category = input("Enter the category of the expense: ")
    description = input("Enter a short description of the expense: \n   ")

    expense = {'Date': date, 'Amount':  main_currency_amount,  'Category': category,
               'Description': description}
    expenses.append(expense)

    print("Expense added successfully!\n")

    if budgets[category] != 0 and sum(expense['Amount'] for expense in expenses if expense['Category'] == category) > \
            budgets[category]:
        print("Warning: You have exceeded the budget for this category.")

# Function to view expenses
def view_expenses():
    print("{:<12} {:<10} {:<20} {:<30}".format('Date', 'Amount', 'Category', 'Description'))
    print("-" * 72)
    for expense in expenses:
        print("{:<12} {:<10.2f} {:<20} {:<30}".format(expense['Date'].strftime('%d/%m/%Y'), expense['Amount'], expense['Category'], expense['Description']))

# Function to generate reports
def generate_reports():
    choice = input("Enter the type of report you want to generate (monthly, category-wise, or total): ")
    if choice == 'monthly':
        while True:
            month_str = input("Enter the month you want to generate the report for (mm/yyyy): ")
            try:
                month = datetime.datetime.strptime(month_str, '%m/%Y').date()
                break
            except ValueError:
                print("Invalid month format. Please enter the month in the format mm/yyyy.")
        total_expenses = 0
        for expense in expenses:
            if expense['Date'].month == month.month and expense['Date'].year == month.year:
                total_expenses += expense['Amount']
        print("Total expenses for the month: {:.2f}".format(total_expenses))
    elif choice == 'category-wise':
        category = input("Enter the category you want to generate the report for: ")
        total_expenses = 0
        for expense in expenses:
            if expense['Category'] == category:
                total_expenses += expense['Amount']
        print("Total expenses for the category {}: {:.2f}".format(category, total_expenses))
    elif choice == 'total':
        total_expenses = sum(expense['Amount'] for expense in expenses)
        print("Total expenses: {:.2f}".format(total_expenses))
    else:
        print("Invalid choice!")

# Function to set budget for a category
def set_budget():
    main_currency = 'PHP'
    print("Categories:", categories)
    category = input("Enter the category you want to set the budget for: ")
    while category not in categories:
        print("Invalid category. Please choose from the following categories:", categories)
        category = input("Enter the category you want to set the budget for: ")

    budget = float(input("Enter the budget for the category: "))
    currency = input("Enter the currency of the budget: ")
    if currency != 'PHP':
        converted_amount = exchange_rates[currency][main_currency]
        budget = budget * converted_amount
        print("The converted value to PHP is : %.2f\n" % budget)
    else:
        budget = budget
    while currency not in exchange_rates:
        print("Invalid currency. Please choose from the following currencies:", list(exchange_rates.keys()))
        currency = input("Enter the currency of the expense: ")

    budgets[category] = budget
    print("Budget set successfully!")

#Function to view budgets
def view_budgets():
    print("{:<20} {:<10}".format('Category', 'Budget'))
    print("-" * 30)
    for category, budget in budgets.items():
        print("{:<20} {:<10.2f}".format(category, budget))

#Main function
login_page()
while True:
        print("1. Add an expense")
        print("2. View expenses")
        print("3. Generate reports")
        print("4. Set budget")
        print("5. View budgets")
        print("6. Add category")
        print("7. Exit")

        choice = input("\nEnter your choice: ")
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            generate_reports()
        elif choice == '4':
            set_budget()
        elif choice == '5':
            view_budgets()
        elif choice == '6':
            add_category()
        elif choice == '7':
            print("Thank you for using the expense tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")