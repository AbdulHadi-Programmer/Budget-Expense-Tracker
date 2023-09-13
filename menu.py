from std import *
from emp import *
from buss import *


print('Welcome to Budget Expense Manager'.center(100,' '))

while True:
    user = input("Enter who you are (Student, Employee, Businessman): ").capitalize()

    # Check if the user input is valid
    if user in ('Student', 'Employee', 'Businessman'):
        break
    else:
        print('Invalid input. Please enter "Student", "Employee", or "Businessman".')

while True:
    ## Business man Category 
    if user == 'Businessman':
        m_choice = int(input("\nEnter The Option:\n\n1) Sales and Revenue Tracking Function\n2) Employee Salaries and Payroll Function\n3) Cash Flow Tracking Function\n4) Inventory Management Function\n5) Investment Tracking Function\n6) Expenses Tracking Function\nInput: "))
        
        if m_choice == 1: # 'Sales and Revenue Tracking Function'
            print('\n*)Sales and Revenue Tracking Function')
            search = int(input("\nEnter The Option:\n1) Record Sales Transaction\n2) Calculate Total Revenue\n3) View Sales Records\nInput: "))
            # Function Inside Category
            if search == 1: # Record Sales Transaction
                record_sales_transaction()  # You need to implement this function
            elif search == 2: # Calculate Total Revenue
                calculate_total_revenue()   # You need to implement this function
            elif search == 3: # View Sales Records
                view_sales_records()        # You need to implement this function
            else:
                break
            
        elif m_choice == 2: # 'Employee Salaries and Payroll Function'
            print('\n*)Employee Salaries and Payroll Function')
            search_2 = int(input("\nEnter The Option:\n1) Update Employee Salaries\n2) View Employee Salaries\nInput: "))
            # Function Inside Category
            if search_2 == 1:
                update_employee_salaries()
            elif search_2 == 2:
                view_employee_salaries()
            else:
                print("Invalid Input")
                break
                
                
        elif m_choice == 3: # Cash Flow Tracking Function
            print('\n*)Cash Flow Tracking Function')
            search_3 = int(input("\nEnter The Option:\n1) Record Cash Inflow\n2) Record Cash Outflow\n3) View Cashflow Summary\nInput: "))
            # Function Inside Category
            if search_3 == 1:
                record_cash_inflow()
            elif search_3 == 2:
                record_cash_outflow()
            elif search_3 == 3:
                view_cash_flow_summary()
            else:
                print("Invalid Input")
                break
                
        elif m_choice == 4: #  Inventory Management Function
            print('\n*)Inventory Management Function')
            search_4 = int(input("\nEnter The Option:\n1) Add Item to Inventory\n2) Update Item Quantity\n3) View Inventory\nInput: "))
            # Function Inside Category
            if search_4 == 1:
                add_item_to_inventory()
            elif search_4 == 2:
                update_item_quantity()
            elif search_4 == 3:
                view_inventory()
            else:
                break
        elif m_choice == 5: # Investment Tracking Function
            print('\n*)Investment Tracking Function')
            search_5 = int(input("\nEnter The Option:\n1)Add Investment\n2)View Investment\nInput: "))
            # Function Inside Category
            if search_5 == 1:
                add_investment()
            elif search_5 == 2:
                view_investments()
            else:
                print('Invalid Input')
                break
        elif m_choice == 6:
            print('\n*)Expenses Tracking Function')
            search_6 = int(input('Enter The Option:\n1) Record Expense\n2) View Expenses\nInput:-'))
            if search_6 == 1:
                record_expense()
            elif search_6 == 2:
                view_expenses_summary()
            else:
                break
                
    # Employee Category 
    elif user == 'Employee':
        print('\nEmployee Category:')
        # Now At First We Calculate Tax
        if remaining_income == 0 :
            check()

        
        m_choice = int(input("\nEnter The Option:\n1) Saving Control and Budget Control\n2) Expenditure Oversight\nInput: "))
        if m_choice == 1: # Saving and Budget Control
            print('Saving Control and Add Monthly Budget:-')
            search = int(input("\nEnter The Option:\n1) Manage Saving\n2) Add Monthly Budget\n3) Income Manager\nInput: "))
            if search == 1:
                emp_manage_savings() 
            elif search == 2:
                monthly_budget() 
            elif search == 3:
                employee_income_manager() 
            else:
                break
        elif m_choice == 2: # Expenditure Oversight ( Expenses )
            print('\nExpenditure Oversight:-')
            search = int(input("\nEnter The Option:\n1) Income Manager\n2) Expenses Tracker\nInput: "))
            if search == 1:
                employee_income_manager()
            elif search == 2:
                emp_manage_expenses() 

    # Student Category
    elif user == 'Student':
        search = int(input("\nEnter The Option:\n1) Manage Saving\n2) Manage Expenses\nEnter Input:- "))
        if search == 1: # Manage Saving
            std_manage_saving()
        elif search == 2: # Manage Expense, include view and update function 
            std_manage_expenses()
        else:
            break
