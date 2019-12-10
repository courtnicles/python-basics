"""
DATA 200 Fall 2019 Homework 1
Courtney Nguyen
14SEP19
hw1-2.py

"""

## 2) Function that counts and returns number of vowels
def vowel_count(a):
    x = 0
    for i in a:
        if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
            x += 1
        else:
            x = x
    return x

print('Type in a random phrase: ')
user_string = str(input())

print('You typed in: ' + user_string)

print('The number of vowels in that phrase is: ')
vowel_count(user_string)