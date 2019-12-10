"""
DATA 200 Fall 2019 Homework 6
Courtney Nguyen
25OCT19
hw6-2.py

"""

import re
from datetime import datetime

linuxRegex = re.compile(r'''
(\d+\s)                       ## bytes
(\w{3}\s+\d+\s\d{2}:\d{2})    ## last modified date
(\s)                          ## space
(.*$)                         ## file name
''', re.VERBOSE)

total_file_size = []

def regexp(a):
    min_date = datetime.today()
    max_date = datetime
    for i in a:
        rpg = linuxRegex.search(i)
        total_file_size.append(int(rpg.group(1)))
        datetime_object = datetime.strptime(rpg.group(2), '%b %d %H:%M')
        if datetime_object < min_date:
            min_date = datetime_object
            return_minimum = "Earliest Modified File: " + str(rpg.group(2)) + " " + str(rpg.group(4))
        if datetime_object > min_date:
            max_date = datetime_object
            return_maximum = "Latest Modified File: " + str(rpg.group(2)) + " " + str(rpg.group(4))
    print(f'The total file size (in bytes) of all files in the listing: {sum(total_file_size)}')
    print(return_minimum)
    print(return_maximum)

i = "-rwxrwxrwx 1 user user  78995 Dec 25 23:03 DATA200 HW2.pdf"
a = "-rwxrwxrwx 1 user user 163483 Sep  8 03:29 DATA200 HW1.pdf"
b = "-rwxrwxrwx 1 user user  78995 Sep 15 23:03 DATA200 HW2.pdf"
c = "-rwxrwxrwx 1 user user 114964 Sep 29 02:10 DATA200 HW3.pdf"
d = "-rwxrwxrwx 1 user user 108137 Oct  7 23:00 DATA200 HW4.pdf"
e = "-rwxrwxrwx 1 user user  82301 Oct 13 17:13 DATA200 HW5.pdf"
f = "-rwxrwxrwx 1 user user  82301 Oct 13 17:15 testing testing testing.XML"
g = "-rwxrwxrwx 1 user user  78995 Sep 5 23:03 DATA200 HW2.pdf"
h = "-rwxrwxrwx 1 user user  78995 Dec 12 23:03 DATA200 HW2.pdf"
list = [i,a,b,c,d,e,f,g,h]

regexp(list)