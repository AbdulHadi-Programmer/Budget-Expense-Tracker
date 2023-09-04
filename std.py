## Student Category Function 
# Global Var
std_savings = 0
std_expense = {
    'Education': 0,
    'Books': 0,
    'Transportation': 0,
    'Entertainment': 0,
    'food': 0
}
std_total = sum(std_expense.values())

def std_update_expenses():
    global std_total
    for category in std_expense:
        expense_amount = float(input(f"Enter the expense amount for {category}: "))
        std_expense[category] += expense_amount
    std_total = sum(std_expense.values())

def std_view_expense():
    global std_total
    print(f'The total expense is {std_total}')
    print("The List of Expense is: ")
    for index, (key, value) in enumerate(std_expense.items()):
        print(f"{index+1}) {key} and Amount is {value}")
    print(f'The Total Expenses is {std_total}')

def std_manage_expenses():
    global std_expense, std_total
    user = int(input("Enter 0 to Write Expenses or 1 to View Expenses: "))

    if user == 0:
        std_update_expenses()
    elif user == 1:
        std_view_expense()
    else:
        print("Invalid choice.")
        
def std_manage_saving():
    global std_savings
    saving1 = int(input("Enter your Saving: "))
    std_savings += saving1

    choice = input("Do you want to view your saving? (yes/no): ").lower()
    if choice == "yes":
        print(f'The total saving is {std_savings}')
    elif choice == "no":
        print("Alright, your decision not to view your savings has been noted.")
    else:
        print('Invalid Input')
