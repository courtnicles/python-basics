"""
DATA 200 Fall 2019 Homework 2
Courtney Nguyen
20SEP19
hw2-3.py

"""
### 3) File WordCount

## Open and process file content
with open('sonnet.txt', 'r') as txt:
    lines = txt.read()
    words = lines.replace("-", ' ')
    words2 = words.replace("'", ' ')
    words3 = words2.split()
    strip_list = [s.strip("? .!/(;:,)") for s in words3]
    new_list = [s.lower() for s in strip_list]

## Function to count number of occurrences, and put in dictionary
def word_count(a):
    counts = dict()
    for i in a:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    return counts

## Call word_count function to created list
w_c = word_count(new_list)

## Remove all numbers in dictionary
final = {k: v for k, v in w_c.items() if not k.isdigit()}

## Create a new dictionary to calculate length of key, concatenate key/value and
## turn it into a new value
new_dict = {}

for key in final:
    length = len(key)
    if (length > 1) in final:
        del final[key]

for key in final:
    length = len(key)
    concatenate = (key, final[key])
    new_dict.__setitem__(concatenate, length)

## Use OrderedDict to sort the dictionary
from collections import OrderedDict

d_sort = OrderedDict(sorted(final.items(), key = lambda x: x[1], reverse=True))

## Function to return only key/value pairs with specified length
def return_specific(a):
    list = []
    for k,v in d_sort.items():
        if (len(k) == a):
            add = (k,v)
            list.append(add)
    return list[0:15]

## Function to return the list created in previous function
def print_final(a):
    for i in a:
        print(i)

## Function to pass list through the previous 2 functions and print output
def for_num(a):
    for i in a:
        print("Top 15, length of word: " + str(i))
        i_list = return_specific(i)
        print_final(i_list)
        print()

# Homework requirement to print out top 15 most used words and counts by lengths 2 to 10
num_list = [2,3,4,5,6,7,8,9,10]

## Pass hwk requirement through for_num function
print(for_num(num_list))

txt.close()