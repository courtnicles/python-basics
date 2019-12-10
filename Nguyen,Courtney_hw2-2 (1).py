"""
DATA 200 Fall 2019 Homework 2
Courtney Nguyen
20SEP19
hw2-2.py

"""

### 2) File I/O

import csv

# Open the csv file
with open('dcp.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    cls = []
    point = []
    for row in csv_reader:
        cls.append(row[1])
        point.append(row[2])


# Function to find index of class
def find_cls(a):
    over_list = []
    for i in a:
        index_return = []
        for idx, val in enumerate(cls):
            if (val == i):
                index_return.append(idx)
        over_list.append(index_return)
    return over_list

# Function to return element value of the index
def return_point(b):
    over_point = []
    for i in b:
        point_list = []
        for j in i:
            point_list.append(point[j])
        point_list = [int(j) for j in point_list]
        over_point.append(point_list)
    return over_point

# Function to find unique classes of the cls in the CSV
def unique_cls(c):
    unique_list = []
    for i in c:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list

# Function to sum the points for each record
def tally(d):
    tally_list = []
    for i in d:
        tally_point = sum(i)
        tally_list.append(tally_point)
    return tally_list

# Close the read csv section
csv_file.close()

# Generate a list of unique classes from the input
unique_classes = unique_cls(cls)

# Generate a maximum parameter for the number of unique classes
count_variables = len(unique_classes)

# Find the indices of the unique classes and put in a list
index_unique_classes = find_cls(unique_classes)

# Using the indices list, create a new list for the matching points
points_accu = return_point(index_unique_classes)

# Sum the points
sum_of_points = tally(points_accu)

## Write to Text
with open('results.txt', 'w') as results:
    i = 0
    while i < count_variables:
        results.write(unique_classes[i] + ", " + str(sum_of_points[i]) + '\n')
        i = i + 1
results.close()