"""
DATA 200 Fall 2019 Homework 8
Courtney Nguyen
16NOV19
hw8-2.py
"""

def binomial(n,r):
    if n < r:
        return "Invalid input, n cannot be less than r"
    elif (r == 0) or (r == n):
        return 1
    else:
        return binomial(n-1, r-1) + binomial(n-1, r)

n = 5
r = 2
print(f' n = {n}, r = {r}, binomial coefficient = {binomial(n,r)}')


n = 5
r = 0
print(f' n = {n}, r = {r}, binomial coefficient = {binomial(n,r)}')

n = 5
r = 5
print(f' n = {n}, r = {r}, binomial coefficient = {binomial(n,r)}')

n = 7
r = 6
print(f' n = {n}, r = {r}, binomial coefficient = {binomial(n,r)}')

n = 5
r = 6
print(f' n = {n}, r = {r}, binomial coefficient = {binomial(n,r)}')

