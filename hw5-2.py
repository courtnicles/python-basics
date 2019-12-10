"""
DATA 200 Fall 2019 Homework 5
Courtney Nguyen
18OCT19
hw5-2.py

"""

import calendar
from datetime import *
import os

def find_files_created(dir_path, ndays):
    files_list = [x for x in os.listdir(dir_path)]
    files_dict = {}

    now = datetime.now()

    for i in files_list:
        path = str(dir_path) + str('/' + i)

        convert_time = datetime.fromtimestamp(os.path.getctime(path)).strftime('%Y-%m-%d %H:%M:%S')

        datediff = abs((datetime.fromtimestamp(os.path.getctime(path)) - now).days)

        if datediff <= ndays:
            files_dict[i] = convert_time
    for k,v in files_dict.items():
        print(k + ' : ' + v)

path_to_input = 'input/'
find_files_created(path_to_input, 15)