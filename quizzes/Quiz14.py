#!/usr/bin/env python3

"""
CS373: Quiz #14 (7 pts)
"""

""" ----------------------------------------------------------------------
 1. What is a primary key?
    [Basic UML & SQL: Rows & Tables]
    (2 pts)

a minimal unique identifier for each row
"""

""" ----------------------------------------------------------------------
 2. What is the multiplicity of an association?
    [Basic UML & SQL: Associations]
    (2 pts)

how many instances of a class are connected to an instance of another
class
"""

""" ----------------------------------------------------------------------
 3. Rewrite the following using a generator.
    (2 pts)
"""

from operator import sub

assert list(map(sub, [2, 3, 4], [3, 1, 7]))                  == [-1, 2, -3]
assert list(sub(x, y) for x, y in zip([2, 3, 4], [3, 1, 7])) == [-1, 2, -3]
