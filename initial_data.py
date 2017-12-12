import pandas as pd
import csv

print("Welcome to your personal budget tracker!")
print("The following information is required for initial data.")

#initializes list for PART 1
list_first_name = []
list_last_name = []
list_income_amt = []
list_num_bill = []
list_bill_name = []
list_bill_amt = []

#Initilizes lists for part two
list_expenses = []
list_add_budget = []
list_rem_budget = []

#Reading a csv file
df = pd.read_csv("budget_tracker_files.csv")
def income():
    income_amt = input("How much revenue do you receive each month?: $")
    
    if income_amt.isdigit() == True:
        print("Thank you!")
        income_amt = float(income_amt)
        list_income_amt.append(income_amt)
        df['Income Amount'] = list_income_amt
            
    else:
        print("Uh oh, that was not a vaild entry. Please try again.")
        income()

        #Asks for name and amount for each bill

def bill_data():
    income_amt = df['Income Amount']
    num_bill = input("How many bills do you pay per month? (ex. 4): ")

    if num_bill.isdigit() == True:
        num_bill = int(num_bill)
        while num_bill > 0:
            bill_name = input("Enter the name of the bill: ")
            list_bill_name.append(bill_name)
            bill_amt = input("How much do owe for this bill? (ex. 120.50): $ ")

            if bill_amt.isdigit() == True:
                bill_amt = float(bill_amt)
                list_bill_amt.append(bill_amt)  
            else:
                print("Uh oh, that was not a vaild entry. Please try again.")
                bill_data()

            num_bill = num_bill -1

        #creates a column for each bill name
        counter = 0
        for name in list_bill_name:
            column = 'Bill Name '+ str(counter + 1)
            df[column] = name
            counter += 1

        #creates a column for each bill amount
        counter = 0
        for amt in list_bill_amt:
            df['Bill ' + str(counter + 1) + ' Amt'] = amt
            counter += 1
                
    else:
        print("Uh oh, that was not a vaild entry. Please try again.")
        bill_data()
    
    #Adjusts total budget according to their bills   
    df['Total Budget'] = income_amt - sum(list_bill_amt)
    print('Thank you for entering your intial data!')
    
    total_budget =df.get_value(0, 'Total Budget', takeable=False)
    
    print('Your total budget is set at: $' + str(total_budget))
        
#Displays menu options for user to update their budget
def menu():
    print("Menu Selection")
    print("1 = Add expense")
    print("2 = Add Revenue")
    print("3 = Remove Revenue")
    print("4 = Exit")
    print("")

    choice = int(input("Enter selection: "))
    
    #Adding an expense
    if choice == 1:
        add_exp_amt = input("Please enter how much you spent (ex. 12.54): $")
        if add_exp_amt.isdigit() == True:
            add_exp_amt = float(add_exp_amt)
            list_expenses.append(add_exp_amt)
            menu_opt()
        else:
            print("Uh oh, that was not a vaild entry. Please try again.")
            print("")
            menu()
    
    #Adding revenue
    elif choice == 2:
        add_rev_amt = input("Please enter how much revenue you received (ex. 12.54): $")
        if add_rev_amt.isdigit() == True:
            add_rev_amt = float(add_rev_amt)
            list_add_budget.append(add_rev_amt)
            menu_opt()
        else:
            print("Uh oh, that was not a vaild entry. Please try again.")
            print("")
            menu()   
      
    #Removing revenue
    elif choice == 3:
        rem_rev_amt = input("Please enter how much revenue you are removing (ex. 12.54): $")
        if rem_rev_amt.isdigit() == True:
            rem_rev_amt = float(rem_rev_amt)
            list_rem_budget.append(rem_rev_amt)
            menu_opt()
        else:
            print("Uh oh, that was not a vaild entry. Please try again.")
            print("")
            menu()   
    
    #Exitting the menu
    elif choice == 4:
        print("Thank you! See you next time.")
        
    else:
        print("That is not a valid choice. Please enter a number 1-5")
        print("")
        menu()

#The option to go back to the menu
def menu_opt():
    option = input("Would you like to go back to the menu? (Y or N): ")
    
    if option.lower() == 'y':
        menu()  
    elif option.lower() == 'n':
        print("Thank you! See you next time.")
    else:
        print("I'm sorry. Please enter a valid option.")
        menu_opt()

#This open is for the end of part 1. Will ask if the user wants to continue with updating their data.
def update_question():
    option_update = input("Would you like to update your budget? (Y or N): ")
    
    if option_update.lower() == 'y':
        menu()  
    elif option_update.lower() == 'n':
        print("Thank you! See you next time.")
    else:
        print("I'm sorry. Please enter a valid option.")
        update_question()

#Start of user input
#User enters name
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")

#Adds name to list
list_first_name.append(first_name.title())
list_last_name.append(last_name.title())

#Creates columns to create dataframe
df['First Name'] = list_first_name
df['Last Name'] = list_last_name

#Greets users and runs income()
print("\nHello "+ first_name.title() + " " + last_name.title() + "!")

income()
bill_data()
update_question()

#Creates an expense column
df['Expenses'] = sum(list_expenses)

#Updates total budget
df['Total Budget'] = df['Total Budget'] + sum(list_add_budget) - sum(list_rem_budget)
total_budget =df.get_value(0, 'Total Budget', takeable=False)
print('Your total budget is set at: $' + str(total_budget))

print(df)
