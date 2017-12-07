"""
    Lorraine Siochi, Emi Vo, Grace Zhang
    INST126 Personal Budget Tracker
    16 December 2017
"""

#This program will receive the initial data to create a budget tracker.

import pandas as pd
import csv

print("Welcome to your personal budget tracker!")
print("The following information is required for initial data.")

list_first_name = []
list_last_name = []
list_income_name = []
list_num_income = []
list_income_amt = []
list_num_bill = []
list_bill_name = []
list_bill_amt = []
list_bill_occur = []
list_bill_date = []


df = pd.DataFrame({"First Name": list_first_name,
    "Last Name":list_last_name,
    "Income Name":list_income_name,
    "Income Amt":list_income_amt,
    """Bill Name":list_bill_name,
    "Bill Amount":list_bill_amt,
                 """}
)

def income():

    num_income = input("How many incomes do you have?: ")
    
    if num_income.isdigit() == True:
        num_income = int(num_income)
        
        while num_income > 0:
            income_name = input("Enter the name of the income source: ")
            list_income_name.append(income_name)
            income_amt = float(input("How much do you make per month with this income?: $"))
            print()
            num_income -= 1
            

        for name in list_income_name:
            counter = 1
            df['Income ' + str(counter) + " Name"] = name
            counter += 1

    else:
        print("Uh oh, that was not a vaild entry. Please try again.")
        income()

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")

list_first_name.append(first_name.title())
list_last_name.append(last_name.title())

print("\nHello "+ first_name.title() + " " + last_name.title() + "!")
income()


num_bill = int(input("How many bills do you pay per month?: "))
list_num_bill.append(num_bill)

while num_bill > 0:
    bill_name = input("Enter the name of the bill: ")
    bill_amt = float(input("How much do owe for this bill?: "))
    bill_occur = int(input("How often does this bill occur (in days): "))
    bill_date = input("When do you pay this bill (MM/DD): ")
    num_bill -= 1
