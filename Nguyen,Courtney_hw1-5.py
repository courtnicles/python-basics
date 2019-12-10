"""
DATA 200 Fall 2019 Homework 1
Courtney Nguyen
14SEP19
hw1-5.py

"""

## 5) List Comprehension
##a) [1, 2, 4, 8, 16, 32, 64, 128, 256] 
l = list(range(9))
a = [ (2**i) for i in l ]
print(a)

##b) [4, 16, 36, 64, 100]
j = list(range(2,11,2))
b = [ i**2 for i in j ]
print(b)

##c) [0, 2, 6, 12, 20, 30, 42, 56, 72, 90] 
k = list(range(1,11))
c = [ i*(i-1) for i in k ]
print(c)