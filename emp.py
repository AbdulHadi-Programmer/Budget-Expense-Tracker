## Employee Function
emp_expense = {
    'Education': 0,
    'Books': 0,
    'Transportation': 0,
    'Entertainment': 0,
    'food': 0
}
saving = 0
total = sum(emp_expense.values())

# Global variables to store income, remaining income, and tax percentage
income = 0
remaining_income = 0
tax_percentage = 0


def calculate_tax(income, tax_percentage):
    tax = (income * tax_percentage) / 100
    return tax

def get_income_and_tax():
    global income, tax_percentage
    income = float(input("Enter your income: "))
    tax_percentage = float(input("Enter tax percentage: "))
    return income, tax_percentage

def main():
    global income, remaining_income, tax_percentage

    if income == 0:
        get_income_and_tax()

    tax = calculate_tax(income, tax_percentage)
    remaining_income = income - tax

    print(f"Tax: {tax}")
    print(f"Remaining Income: {remaining_income}")

def check():
    global remaining_income
    if remaining_income == 0:
        main()
    else:
        pass

# 02

def monthly_budget():
    global m_budget ,remaining_income
    m_budget = int(input("Enter Your Monthly Budget: "))
    print(f'Your Monthly Budget is: {m_budget}')
    remaining_income  -= m_budget
    print(f'Your Remaining Income is: {remaining_income}')
    return m_budget

def emp_manage_savings():
    global saving, remaining_income
    
    saving1 = int(input('Enter the Saving: '))
    remaining_income  -= saving1     # Calculate remaining_income
    
    saving += saving1
    print(f'Your Current Saving Amount is: {saving}')
    print(f'Your remaining income: {remaining_income}')

def emp_update_expenses(emp_expense):
    global total, remaining_income
    
    for category in emp_expense:
        expense_amount = float(input(f"Enter the expense amount for {category}: "))
        emp_expense[category] += expense_amount
    

def emp_view_expense(emp_expense):
    global total, remaining_income
    total = sum(emp_expense.values())
    print("The List of Expense is: ")
    for index, (key, value) in enumerate(emp_expense.items()):
        print(f"{index+1}) {key} and Amount is {value}")
    print(f'The Total Expenses is {total}')
    print(f"Remaining Income after subtracting Expenses Amount: {remaining_income - total}")
    
def emp_manage_expenses():
    user_choice = int(input("Enter 0 to Write Expenses or 1 to View Expenses: "))
    
    if user_choice == 0:
        emp_update_expenses(emp_expense)
        #print(f"Remaining Income after subtracting Expenses Amount: {remaining_income}")
    elif user_choice == 1:
        emp_view_expense(emp_expense)
        #print(f"Remaining Income after subtracting Expenses Amount: {remaining_income}")
    else:
        print("Invalid choice.")



# # Other Functions 
def employee_income_manager():
    global remaining_income, total
    choice = input("Do you want to add/view employee income? (add/view/exit): ").lower()

    if choice == "add":
        income1 = int(input("Enter the New Income: "))
        remaining_income += income1
        print("Employee income added.")
    elif choice == "view":
        if total > 0:
            print(f"The Employee's total expenses are: {total}")
            remaining_after_expenses = remaining_income - total
            print('Remaining Income After Expenses:',remaining_after_expenses)
            if remaining_after_expenses < 0:
                print("Warning: Expenses exceed income.")
            else:
                print(f"The Employee's remaining income after expenses: {remaining_after_expenses}")
        else:
            print(f"The Employee's income is: {remaining_income}")
    elif choice == "exit":
        print("Exiting employee income manager.")
    else:
        print("Invalid choice.")