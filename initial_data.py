"""
    Lorraine Siochi, Emi Vo, Grace Zhang
    INST126 Personal Budget Tracker
    16 December 2017
"""

#This program will receive the initial data to create a budget tracker.

import pandas as pd

print("Welcome to your personal budget tracker!")

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")

income_str = input("How many incomes do you have?")
income_num = int(income_str)

while income_num > 0:
    income_name = input("Enter the name of the income source: ")
    income_amt = input("How much do you make per month with this income?: ")
    income_num -= income_num