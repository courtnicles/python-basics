"""
DATA 200 Fall 2019 Homework 1
Courtney Nguyen
14SEP19
hw1-3.py

"""

## 3) Decimal Extractor

while True:
    print('Enter a number: (Type "end" to exit)')
    user_input = input()
    if user_input == "end":
        break
    value = float(user_input) 
    decimal = value % 1
    print (decimal)
