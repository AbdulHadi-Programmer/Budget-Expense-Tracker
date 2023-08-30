## Businessman function file 
## Global Var

inventory = {} # name , quantity and price per unit and total
sales_records = [] # Sales Record 

investments = {} # Name and amount 

cash_inflows = [] # Cash Amount IN
cash_outflows = [] # Cash Amount OUT

emp_salaries = {}  # Create an empty dictionary to store employee salaries  04
total_payroll = 0 # Total emp salaries
total_revenue = 0  # Placeholder for total revenue (You should implement this calculation)

expense = {} # And 
total_expense = 0
# Function To calculate net worth 
def profit_and_loss_calculation(net_profit, total_expenses, total_revenue):
    total_revenue = calculate_total_revenue()
    total_expenses = calculate_total_expenses()
    net_profit = total_revenue - total_expenses
    return net_profit
    

# Function to update employee salaries  
def update_employee_salaries():
    global emp_salaries, total_payroll
    num_employees = int(input("Enter the number of employees: "))
    
    for _ in range(num_employees):
        employee_name = input("Enter the name of the employee: ")
        salary = float(input(f"Enter the salary for {employee_name}: "))
        emp_salaries[employee_name] = salary
    print("Employee salaries updated.")
    user = int(input("Enter 1 For viewing the total payroll and 0 for exit: "))
    
    total_payroll = sum(emp_salaries.values())
    print(f'The Total Payroll of Employee are: {total_payroll}')


def view_employee_salaries():
    global total_payroll  # Declare total_payroll as global here
    total_payroll = sum(emp_salaries.values())
    print("Employee Salaries:")
    for employee, salary in emp_salaries.items():
        print(f"{employee}: {salary}")
    print(f'Total Payroll: {total_payroll}')
    

# Function to record a Sales Transaction   01 part
def record_sales_transaction():
    item_name = input("Enter the name of the item sold: ")
    quantity = int(input("Enter the quantity sold: "))
    price_per_unit = float(input("Enter the price per unit: "))
    
    total_price = quantity * price_per_unit
    sales_records.append({'item': item_name, 'quantity': quantity, 'price_per_unit': price_per_unit, 'total_price': total_price})
    
    print(f"Sales transaction for {quantity} {item_name}(s) recorded. Total amount: {total_price}")

# Function to calculate total revenue   01 part
def calculate_total_revenue():
    total_revenue = sum(record['total_price'] for record in sales_records)
    print(f'The Total Revenue is :{total_revenue}')
    return total_revenue

# Function to view sales records and total revenue   01 part
def view_sales_records():
    global total_revenue
    total_revenue = calculate_total_revenue()
    
    print("Sales Records:")
    for record in sales_records:
        print(f"Item: {record['item']}, Quantity: {record['quantity']}, Price per Unit: {record['price_per_unit']}, Total Amount: {record['total_price']}")
    
    print(f'Total Revenue: {total_revenue}')



### Cash Flow Tracking Function ### 02
# Function to record cash inflow
def record_cash_inflow():
    amount = float(input("Enter the amount of cash inflow: "))
    reason = input("Enter the reason for cash inflow: ")
    cash_inflows.append({'amount': amount, 'reason': reason})
    print("Cash inflow recorded.")

# Function to record cash outflow
def record_cash_outflow():
    amount = float(input("Enter the amount of cash outflow: "))
    reason = input("Enter the reason for cash outflow: ")
    cash_outflows.append({'amount': amount, 'reason': reason})
    print("Cash outflow recorded.")

# Function to view cash flow summary
def view_cash_flow_summary():
    total_inflows = sum(item['amount'] for item in cash_inflows)
    total_outflows = sum(item['amount'] for item in cash_outflows)
    net_cash_flow = total_inflows - total_outflows

    print("Cash Flow Summary:")
    print(f"Total Inflows: {total_inflows}")
    print(f"Total Outflows: {total_outflows}")
    print(f"Net Cash Flow: {net_cash_flow}")


### Inventory Management Function ###  03
# Function to add a new item to the inventory
def add_item_to_inventory():
    item_name = input("Enter the name of the item: ")
    quantity = int(input("Enter the quantity of the item: "))
    price_per_unit = float(input("Enter the price per unit: "))
    inventory[item_name] = {'quantity': quantity, 'price_per_unit': price_per_unit}
    print("Item added to inventory.")

# Function to update the quantity of an item in the inventory
def update_item_quantity():
    item_name = input("Enter the name of the item: ")
    if item_name in inventory:
        new_quantity = int(input("Enter the new quantity: "))
        inventory[item_name]['quantity'] = new_quantity
        print("Item quantity updated.")
    else:
        print("Item not found in inventory.")

# Function to view the inventory
def view_inventory():
    print("Inventory:")
    for item, details in inventory.items():
        print(f"Item: {item}, Quantity: {details['quantity']}, Price per Unit: {details['price_per_unit']}")



### Investment Tracking Function ###  04
# Function to add a new investment
def add_investment():
    investment_name = input("Enter the name of the investment: ")
    investment_amount = float(input("Enter the amount of the investment: "))
    expected_return = float(input("Enter the expected return on investment: "))
    investments[investment_name] = {'amount': investment_amount, 'return': expected_return}
    print("Investment added.")

# Function to view all investments
def view_investments():
    print("List of Investments:")
    for investment, details in investments.items():
        print(f"Name: {investment}, Amount: {details['amount']}, Expected Return: {details['return']}")



def calculate_total_expenses():
    global total_expenses
    total_expenses = sum(expense['amount'] for expense in expense)  # Use "expense" here
    return total_expenses

### Expenses Tracking Function ###  05
# Function to record an expense
def record_expense():
    expense_name = input("Enter the name of the expense: ")
    amount = float(input("Enter the amount of the expense: "))
    expense[expense_name] = {'amount': amount}
    print("Expense recorded.")

# Function to view expenses summary
def view_expenses_summary():
    global total_expenses
    total_expenses = sum(item['amount'] for item in expense.values())
    
    print("Expenses Summary:")
    for expense_name, details in expense.items():
        print(f"Expense: {expense_name}, Amount: {details['amount']}")
    
    print(f'Total Expenses: {total_expenses}')
