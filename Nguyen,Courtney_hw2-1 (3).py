"""
DATA 200 Fall 2019 Homework 2
Courtney Nguyen
20SEP19
hw2-1.py

"""

## 1) List Overlap

my_list = ['my', 'dog', 'is', 'a', 'demon']
my_other_list = ['i', 'should', 'have', 'a', 'cat', 'instead']

print(my_list, my_other_list)

def find_list_overlap(list1,list2):
    a = set(list1)
    b = set(list2)
    overlap = a & b
    overlap_list = list(overlap)
    return overlap_list

print(find_list_overlap(my_list,my_other_list))

