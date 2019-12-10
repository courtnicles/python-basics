"""
DATA 200 Fall 2019 Homework 3
Courtney Nguyen
04OCT19
hw3-1.py

"""

import json, os, csv

## find directory and write to list JSON files only, handling any number of files
path_to_input = 'input/'
json_files_list = [x for x in os.listdir(path_to_input) if x.endswith('.json')]
os.chdir("input/")

user_steps = dict()
json_save = list()

## save each JSON dictionary to a list
for i in json_files_list:
    with open(i) as json_file:
        content = json.load(json_file)
        json_save.append(content)

## save dictionaries in list to new dictionary based on user key
for i in json_save:
    user_steps[i['user']] = user_steps.get(i['user'], 0) + int(i['steps'])

## sort dictionary by points
from collections import OrderedDict
steps_sort = OrderedDict(sorted(user_steps.items(), key = lambda x: x[1], reverse=True))

## write header and dictionary values to a CSV file
out_file = 'leaderboard.csv'
header = ['user','total_steps']
with open(out_file, 'w', newline='') as tally_points:
    writer = csv.writer(tally_points)
    writer.writerow(header)
    for i in steps_sort.items():
        writer.writerow(i)



