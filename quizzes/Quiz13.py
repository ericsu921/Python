#!/usr/bin/env python3

"""
CS373: Quiz #13 (7 pts)
"""

""" ----------------------------------------------------------------------
 1. What's the output of the following?
    What is f() computing?
    (6 pts)

False
True
1
1
2
3
1
Fibonacci
"""

def f () :
    x, y = 1, 1
    while True :
        yield x
        x, y = y, x + y

p = f()
q = f()
print(p is q)
r = iter(p)
print(r is p)
v = next(p)
print(v)
v = next(p)
print(v)
v = next(p)
print(v)
v = next(p)
print(v)
v = next(q)
print(v)
