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

#Trying to create eh dataframe

def income():
    income_amt = input("How much revenue to receive each month?: $")
    
    if income_amt.isdigit() == True:
        print("Thank you!")
        income_amt = float(income_amt)
        list_income_amt.append(income_amt)
            
    else:
        print("Uh oh, that was not a vaild entry. Please try again.")
        income()

        

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")

list_first_name.append(first_name.title())
list_last_name.append(last_name.title())

print("\nHello "+ first_name.title() + " " + last_name.title() + "!")
income()

print(list_first_name)
print(list_last_name)
print(list_income_amt)
    
df = pd.DataFrame
(
    {"First Name": list_first_name,
    "Last Name": list_last_name,
    "Income Amt":list_income_amt}
)


num_bill = int(input("How many bills do you pay per month?: "))
list_num_bill.append(num_bill)

while num_bill > 0:
    bill_name = input("Enter the name of the bill: ")
    bill_amt = float(input("How much do owe for this bill?: "))
    bill_occur = int(input("How often does this bill occur (in days): "))
    bill_date = input("When do you pay this bill (MM/DD): ")
    num_bill -= 1
