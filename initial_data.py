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

while num_bill > 0:
    bill_name = input("Enter the name of the bill: ")
    list_bill_name.append(bill_name)
    bill_amt = float(input("How much do owe for this bill?: "))
    list_bill_amt.append(bill_amt)   
    num_bill = num_bill -1
    
print(list_bill_name)
print(list_bill_amt)
    
for name in list_bill_name:
    counter = 0
    column = 'Bill Name '+ str(counter + 1)
    df[column] = name
    counter += 1
    
for amt in list_bill_amt:
    counter = 0
    df['Bill ' + str(counter + 1) + 'Amt'] = amt
    counter += 1
