"""
DATA 200 Fall 2019 Homework 6
Courtney Nguyen
25OCT19
hw6-1.py

"""

class MyQueue:

    def __init__(self, name, q = []): ## constructor to initialize object
        self.name = name
        self.q = q

    def is_empty(self): ## method to check if MyQueue object is empty, true if condition is true
        if len(self.q) == 0:
            print(True)
        else:
            print(False)

    def queue(self, item): ## append list with new element
        self.q.append(item)

    def dequeue(self): ## remove and return 1st added element
        print(self.q.pop(0))

    def print_queue(self): ## print list of elements in order
        print(self.q)


a = MyQueue('a')
a.is_empty()

a.queue('add')
a.queue('this')
a.queue('word')
a.print_queue()

a.is_empty()
a.queue('aaa')
a.queue('AAA')
a.queue('zzz')
a.print_queue()

a.dequeue()