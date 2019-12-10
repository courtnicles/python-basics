"""
DATA 200 Fall 2019 Homework 8
Courtney Nguyen
16NOV19
hw8-1.py
"""

import re
from queue import LifoQueue

def check_html_balance(html):
    line = re.split('(<[^>]*>)', html)[1::2]
    stack = LifoQueue()
    for word in line:
        if ('/' not in word):
            stack.put(word)
        elif not stack.empty():
            stack.get()
    if stack.empty() == True:
        print("This html document is balanced and therefore valid.")
    else:
        print("This html document is not balanced and therefore invalid.")

## test section

text='''<html>
    <head>
    <title>
    Example
    </title>
    </head>
    <body>
    <h1>Hello, world</h1>
    </body>
    </html>'''

text2='''<html>
    <head>
    <title>
    Example
    </title>
    </head>
    <body>
    <h1>Hello, world</h1>

    </html>'''

check_html_balance(text)
check_html_balance(text2)