"""
DATA 200 Fall 2019 Homework 1
Courtney Nguyen
14SEP19
hw1-1.py

"""

## 1) Euclidean norm

import math

list = [1,2,3,4,5]

def norm(v,p = 2):
    for i in v:
        eucl = math.sqrt((i**2) + (p**2))
        print ("The Euclidean norm of " + str(i) + " with p = 2 is " +
               str(eucl))
norm(list)

