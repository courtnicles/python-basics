"""
DATA 200 Fall 2019 Homework 1
Courtney Nguyen
14SEP19
hw1-6.py

"""

## 6) New Heights Filtered
heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]
new_heights_filtered = [x+5 for x in heights if x > 155 and x <= 164]
new_heights_filtered