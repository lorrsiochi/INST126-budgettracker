"""
    Lorraine Siochi, Emi Vo, Grace Zhang
    INST126 Personal Budget Tracker
    16 December 2017
"""

#This program will receive the initial data to create a budget tracker.

import pandas as pd
import csv

print("Welcome to your personal budget tracker!/n")
print("The following information is required for initial data.")


first_name = input("Enter first name: ")
last_name = input("Enter last name: ")

num_income = int(input("How many incomes do you have?"))
while num_income > 0:
    income_name = input("Enter the name of the income source: ")
    income_amt = float(input("How much do you make per month with this income?: "))
    num_income -= num_income

num_bill = int(input("How many bills do you pay per month?: "))
while num_bill > 0:
    bill_name = input("Enter the name of the bill: ")
    bill_amt = float(input("How much do owe for this bill?: "))
    bill_occur = int(input("How often does this bill occur (in days): "))
    bill_date = input("When do you pay this bill (MM/DD): ")
    num_bill -= num_bill
    
