"""
Calculating with Functions
https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39/train/python
"""

#Solution Codewars
def zero(f = None): return 0 if not f else f(0)
def one(f = None): return 1 if not f else f(1)
def two(f = None): return 2 if not f else f(2)
def three(f = None): return 3 if not f else f(3)
def four(f = None): return 4 if not f else f(4)
def five(f = None): return 5 if not f else f(5)
def six(f = None): return 6 if not f else f(6)
def seven(f = None): return 7 if not f else f(7)
def eight(f = None): return 8 if not f else f(8)
def nine(f = None): return 9 if not f else f(9)

def plus(y): return lambda x: x+y
def minus(y): return lambda x: x-y
def times(y): return lambda  x: x*y
def divided_by(y): return lambda  x: x/y

# Solution ChatGPT
def zero(op=None):
    if op:
        return op(0)
    return 0

def one(op=None):
    if op:
        return op(1)
    return 1

def two(op=None):
    if op:
        return op(2)
    return 2

def three(op=None):
    if op:
        return op(3)
    return 3

def four(op=None):
    if op:
        return op(4)
    return 4

def five(op=None):
    if op:
        return op(5)
    return 5

def six(op=None):
    if op:
        return op(6)
    return 6

def seven(op=None):
    if op:
        return op(7)
    return 7

def eight(op=None):
    if op:
        return op(8)
    return 8

def nine(op=None):
    if op:
        return op(9)
    return 9

def plus(x):
    def inner(y):
        return x + y
    return inner

def minus(x):
    def inner(y):
        return x - y
    return inner

def times(x):
    def inner(y):
        return x * y
    return inner

def divided_by(x):
    def inner(y):
        return x // y
    return inner


