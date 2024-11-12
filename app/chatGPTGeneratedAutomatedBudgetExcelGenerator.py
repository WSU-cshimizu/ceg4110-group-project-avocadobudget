import csv
import random
from datetime import datetime, timedelta

# Define expense categories and target percentages (total must sum to 100)
categories = ['rent', 'groceries', 'entertainment', 'miscellaneous', 'bills/subscriptions', 'savings']
payment_methods = ['Cash', 'Credit Card', 'Debit Card', 'Checking', '3rd Party Payment']

# Define target percentages for each category
category_percentages = {
    'rent': 25,
    'groceries': 20,
    'entertainment': 15,
    'miscellaneous': 15,
    'bills/subscriptions': 15,
    'savings': 10
}

# List of specific descriptions for each category
groceries_descriptions = [
    "Fresh produce", 
    "Snacks", 
    "Meat/seafood", 
    "Dairy products", 
    "Beverages", 
    "Frozen food", 
    "Household supplies"
]

entertainment_descriptions = [
    "Movie ticket",
    "Concert ticket",
    "Streaming service (Spotify, Apple Music)",
    "Dining out (restaurant)",
    "Event (sports, theater, etc.)",
    "Hobby-related (books, games, etc.)"
]

miscellaneous_descriptions = [
    "Clothing purchase",
    "Personal care (haircut, beauty products)",
    "Gift (birthday, holiday)",
    "Household items",
    "Pet expenses",
    "Travel expenses (day trips)",
    "Charity donation"
]

# Function to generate a random expense for a given category
def generate_random_expense(expense_id, start_date, category, category_total, descriptions):
    if not descriptions:  # Check if the descriptions list is empty
        raise ValueError(f"Descriptions list for {category} is empty. Cannot generate expense.")
    
    description = random.choice(descriptions)  # Randomly select a description for the category
    
    # Randomly generate an expense amount within the category's budget
    amount = round(random.uniform(0.1, 1.0) * category_total, 2)  # Distribute the total budget randomly
    if amount == 0:
        amount = 0.01  # Prevent zero amounts
    
    payment_method = random.choice(payment_methods)
    expense_date = start_date.strftime('%Y-%m-%d')
    
    return [expense_id, category, description, amount, expense_date, payment_method]

# Function to generate total expenses for each category based on percentages
def generate_category_totals(annual_expense, category_percentages):
    total_amount_per_category = {}
    for category, percentage in category_percentages.items():
        total_amount_per_category[category] = (annual_expense * percentage / 100)
    return total_amount_per_category

# Starting date for expenses
start_date = datetime(2024, 1, 1)

# Set the total annual expense budget (this can be any value you choose)
annual_expense_budget = 24000.00  # Example: $12,000 total for the year

# Generate total amount for each category
total_amount_per_category = generate_category_totals(annual_expense_budget, category_percentages)

# Create a list to store the data
expenses_data = []

# For each month, generate rent entry and random daily expenses for other categories
expense_id = 1
for month in range(1, 13):  # Loop through each month
    # Set the first day of the month and last day of the month
    month_start_date = datetime(2024, month, 1)
    # Calculate the number of days in the month
    next_month = month % 12 + 1
    month_end_date = datetime(2024, next_month, 1) - timedelta(days=1)
    num_days_in_month = (month_end_date - month_start_date).days + 1

    # Ensure num_days_in_month is valid and greater than 0
    if num_days_in_month <= 0:
        print(f"Error: Invalid month date range for {month_start_date.strftime('%B %Y')}")
        continue

    # Rent: One entry per month
    rent_amount = total_amount_per_category['rent'] / 12  # Spread rent across 12 months
    expenses_data.append([expense_id, 'rent', 'Monthly rent payment', round(rent_amount, 2), month_start_date.strftime('%Y-%m-%d'), random.choice(payment_methods)])
    expense_id += 1

    # Grocery: At least one entry per month
    grocery_amount = total_amount_per_category['groceries'] / 12  # Spread groceries across 12 months
    grocery_day = random.randint(0, num_days_in_month - 1)
    grocery_date = month_start_date + timedelta(days=grocery_day)
    expenses_data.append([expense_id, 'groceries', 'Grocery shopping', round(grocery_amount, 2), grocery_date.strftime('%Y-%m-%d'), random.choice(payment_methods)])
    expense_id += 1

    # Savings: Exactly one entry per month, randomly placed
    savings_amount = total_amount_per_category['savings'] / 12  # Spread savings across 12 months
    savings_day = random.randint(0, num_days_in_month - 1)
    savings_date = month_start_date + timedelta(days=savings_day)
    expenses_data.append([expense_id, 'savings', 'Monthly savings', round(savings_amount, 2), savings_date.strftime('%Y-%m-%d'), random.choice(payment_methods)])
    expense_id += 1

    # Bills/Subscriptions: Randomly select specific bills for each month
    num_bills = random.randint(1, 3)  # Generate 1 to 3 bill entries per month
    for _ in range(num_bills):
        bill_category = 'bills/subscriptions'
        bill_description = random.choice([
            "Internet bill",
            "Phone bill",
            "Netflix subscription",
            "Spotify subscription",
            "Gym membership",
            "Electricity bill",
            "Water bill",
            "Cable TV",
            "Hulu subscription",
            "Disney+ subscription",
            "Amazon Prime subscription",
            "Trash collection fee",
            "Home security system",
            "Cloud storage subscription",
            "Insurance payment"
        ])  # Randomly select a bill description
        bill_amount = total_amount_per_category[bill_category] / 12  # Spread bills across 12 months
        bill_day = random.randint(0, num_days_in_month - 1)
        bill_date = month_start_date + timedelta(days=bill_day)
        expenses_data.append([expense_id, bill_category, bill_description, round(bill_amount, 2), bill_date.strftime('%Y-%m-%d'), random.choice(payment_methods)])
        expense_id += 1

    # Miscellaneous: Randomly select specific miscellaneous expenses for the month
    num_miscellaneous = random.randint(1, 3)  # Generate 1 to 3 miscellaneous entries per month
    for _ in range(num_miscellaneous):
        try:
            expenses_data.append(generate_random_expense(expense_id, month_start_date, 'miscellaneous', total_amount_per_category['miscellaneous'], miscellaneous_descriptions))
        except ValueError as e:
            print(f"Error generating miscellaneous expense: {e}")
        expense_id += 1

    # Entertainment: Randomly select specific entertainment expenses for the month
    num_entertainment = random.randint(1, 3)  # Generate 1 to 3 entertainment entries per month
    for _ in range(num_entertainment):
        try:
            expenses_data.append(generate_random_expense(expense_id, month_start_date, 'entertainment', total_amount_per_category['entertainment'], entertainment_descriptions))
        except ValueError as e:
            print(f"Error generating entertainment expense: {e}")
        expense_id += 1

    # Other categories: Ensure at least 20 expenses per month
    num_other_expenses = 20 - 3 - num_bills - num_miscellaneous - num_entertainment  # Adjust for rent, groceries, savings, bills, and other selected categories
    other_categories = ['rent', 'groceries', 'savings', 'bills/subscriptions', 'miscellaneous', 'entertainment']
    
    for _ in range(num_other_expenses):
        # Randomly pick a category that needs more expenses
        valid_categories = [cat for cat in categories if cat not in other_categories]
        if valid_categories:
            category = random.choice(valid_categories)
            category_total = total_amount_per_category[category] / 12  # Distribute across 12 months
            expense_date = month_start_date + timedelta(days=random.randint(0, num_days_in_month - 1))
            expense_data = generate_random_expense(expense_id, expense_date, category, category_total, ['Miscellaneous'])  # Placeholder for actual category
            expenses_data.append(expense_data)
            expense_id += 1
        else:
            print("No valid categories left to generate expenses for.")
            break

# Write to CSV file
with open('yearly_expenses_with_all_categories.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['expense_id', 'expense_categories', 'expense_description', 'expense_amount', 'expense_date', 'expense_payment_method'])
    writer.writerows(expenses_data)

print("CSV file 'yearly_expenses_with_all_categories.csv' has been generated.")
