import pandas as pd
import csv

print("Welcome to your personal budget tracker!")
print("The following information is required for initial data.")

list_first_name = []
list_last_name = []
list_income_amt = []
list_num_bill = []
list_bill_name = []
list_bill_amt = []
list_bill_occur = []
list_bill_date = []

#Trying to create a dataframe
df = pd.read_csv("budget_tracker_files.csv")

def income():
    income_amt = input("How much revenue do you receive each month?: $")
    
    if income_amt.isdigit() == True:
        print("Thank you!")
        income_amt = float(income_amt)
        list_income_amt.append(income_amt)
        df['Income Amount'] = income_amt
            
    else:
        print("Uh oh, that was not a vaild entry. Please try again.")
        income()

df = pd.read_csv('budget_tracker_files.csv')

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")



list_first_name.append(first_name.title())
list_last_name.append(last_name.title())

df['First Name'] = list_first_name
df['Last Name'] = list_last_name

print("\nHello "+ first_name.title() + " " + last_name.title() + "!")
income()

num_bill = int(input("How many bills do you pay per month?: "))
bill_name = ''
while num_bill > 0:
    bill_name = input("Enter the name of the bill: ")
    list_bill_name.append(bill_name)
    bill_amt = float(input("How much do owe for this bill?: "))
    list_bill_amt.append(bill_amt)   
    num_bill = num_bill -1
    
print(list_bill_name)
print(list_bill_amt)
counter = 0

for name in list_bill_name:
    column = 'Bill Name '+ str(counter + 1)
    df[column] = name
    counter += 1

counter = 0
for amt in list_bill_amt:
    df['Bill ' + str(counter + 1) + ' Amt'] = amt
    counter += 1

    
def menu():
    print("Menu Selection")
    print("1 = Add expense")
    print("2 = Add Revenue")
    print("3 = Remove Revenue")
    print("4 = Exit")

    choice = int(input("Enter selection: "))
    if choice == 1:
        add_exp_amt = float(input("Please enter how much you spent (ex. 12.54): $"))
        menu_opt()
    elif choice == 2:
        add_rev_amt = input("Please enter how much revenue you received (ex. 12.54): $")
        menu_opt()
    elif choice == 3:
        expense_amt = input("Please enter how much revenue you are removing (ex. 12.54): $")
        menu_opt()
    elif choice == 4:
        print("Thank you! See you next time.")
    else:
        print("That is not a valid choice. Please enter a number 1-5")
        choice = int(input("Enter selection: "))

def menu_opt():
    option = input("Would you like to go back to the menu? (Y or N): ")
    
    if option.lower() == 'y':
        menu()  
    elif opt.lower() == 'n':
        print("Thank you! See you next time.")
    else:
        print("I'm sorry. Please enter a valid option.")
        menu_opt()

menu()

if choice == 1:
    add_exp_amt = float(input("Please enter how much you spent (ex. 12.54): $"))
    menu_opt()
elif choice == 2:
    add_rev_amt = input("Please enter how much revenue you received (ex. 12.54): $")
    menu_opt()
elif choice == 3:
    expense_amt = input("Please enter how much revenue you are removing (ex. 12.54): $")
    menu_opt()
elif choice == 4:
    print("Thank you! See you next time.")
else:
    print("That is not a valid choice. Please enter a number 1-5")
    choice = int(input("Enter selection: "))
    menu()
