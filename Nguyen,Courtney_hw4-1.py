"""
DATA 200 Fall 2019 Homework 4
Courtney Nguyen
11OCT19
hw4-1.py

"""

import json, os, csv
from collections import Counter

## find directory and write to list JSON files only, handling any number of files
path_to_input = 'input/'
json_files_list = [x for x in os.listdir(path_to_input) if x.endswith('.json')]
os.chdir("input/")

json_save = list()

## save each JSON dictionary to a list
for i in json_files_list:
    with open(i) as json_file:
        content = json.load(json_file)
        json_save.append(content)

## Counter from collections
cnt = Counter()
for i in json_save:
    steps = sum([i['steps']])
    cnt[i['user']] += steps

## write header and dictionary values to a CSV file
out_file = 'leaderboard2.csv'
header = ['user','total_steps']
with open(out_file, 'w', newline='') as tally_points:
    writer = csv.writer(tally_points)
    writer.writerow(header)
    for i in sorted(cnt.items(), key = lambda kv: kv[1], reverse = True):
        writer.writerow(i)







