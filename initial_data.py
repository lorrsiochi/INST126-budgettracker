"""
    Lorraine Siochi, Emi Vo, Grace Zhang
    INST126 Personal Budget Tracker
    16 December 2017
"""

#This program will receive the initial data to create a budget tracker.

import pandas as pd
import csv

print("Welcome to your personal budget tracker!")

# Creating and opening CSV: with open('user_data.csv', 'w', newline='') as ud:
# a = csv.writer(ud, delimeter=',')

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")

income_str = input("How many incomes do you have?")
income_num = int(income_str)
while income_num > 0:
    income_name = input("Enter the name of the income source: ")
    income_amt = input("How much do you make per month with this income?: ")
    income_num -= income_num

bill_str = input("How many bills do you pay per month?: ")
bill_num = int(bill_str)
while bill_num > 0:
    bill_name = input("Enter the name of the bill: ")
    bill_amt = input("How much do owe for this bill?: ")
    bill_occur = input("How often does this bill occur (in days): ")
    bill_date = input("When do you pay this bill (MM/DD): ")
    bill_num -= bill_num
    
# Exporting data into CSV: a.writerows(namehere)
