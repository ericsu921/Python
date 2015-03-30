#!/usr/bin/env python3

"""
CS373: Quiz #11 (7 pts)
"""

""" ----------------------------------------------------------------------
 1. What is the output of the following?
    (6 pts)

m1
m2
f1
m3
f2
m4
f3
m6
"""

def f () :
    print("f1")
    yield f()
    print("f2")
    yield f()
    print("f3")

try :
    print("m1")
    x = f()
    print("m2")
    y = next(x)
    print("m3")
    y = next(x)
    print("m4")
    y = next(x)
    print("m5")
except StopIteration :
    print("m6")
