#!/usr/bin/env python3

# ------------
# Operators.py
# ------------

# https://docs.python.org/3.4/library/operator.html

import operator

print("Operators.py")       # python is strictly an R-value language. it either returns an R-value or it returns nothing

i = 2
j = -i
assert i ==  2
assert j == -2
#-i += 1                    # SyntaxError: illegal expression for augmented assignment...here we are trying to modify the result of negation, well that doesn't make sense bc negation doesn't return an L-value, it returns an R-value. that would be the same as doing -5 += 1. can't be done.

i = 2
j = 3
#k = (i = j)                # SyntaxError: invalid syntax...assignment operator, does not modify j, modifies i, returns nothing
i = j                       # all we can do with an operator that modifies one of its args is use it in a stand-alone way
assert i == 3
assert j == 3

i = 2
j = 3
k = i + j                   # + is a pure R-value kind of fellow, two R-values come in, an R-value comes out
assert i == 2
assert j == 3
assert k == 5
#(i + j) += 1 # SyntaxError: illegal expression for augmented assignment...cannot modify R-value

i = 2                       # Later we're going to see the value of a function that takes as an arg another function, this kind of function is called a higher order function. most common ones are sort(), map() and reduce(). what's going to be attractive about a function like that is to sometimes be able to feed it an operator. you can't actually feed the + sign as an arg to anyone. so python decided to create a module called operator, and in that module, it created a bunch of named functions which are nothing more than the various operators that python comes with. so the operator.add() function is just like the + token effectively. so if we have a higher order function like reduce() that wants a binary function as an arg. we can give reduce() operator.add(). 
j = 3
k = operator.add(i, j)          # pure R-value kind of fellow. takes in 2 R-values and returns an R-value.
assert i == 2
assert j == 3
assert k == 5
#operator.add(i, j) += 1        # SyntaxError: can't assign to function call

i = 2
j = 3
#k = (i += j)                   # SyntaxError: invalid syntax...i += j returns nothing.
i += j                          # can only stand alone
assert i == 5
assert j == 3

i = 4
j = 2
k = i / j                       # true division or floating point division
assert i       == 4
assert j       == 2
assert type(k) is float
assert str(k)  == "2.0"

i =  4
j =  2
i /= j                          # Downing calls this a companion to / operator
assert type(i) is float
assert str(i ) == "2.0"
assert j       == 2

i = 5
j = 2
k = i // j                      # floor division or integer division
assert i       == 5
assert j       == 2
assert type(k) is int
assert k       == 2

i = 5
j = 2
i //= j
assert type(i) is int
assert i == 2
assert j == 2

i = 5.0
j = 2
k = i // j                      # floor division
assert i       == 5.0
assert j       == 2
assert type(k) is float
assert str(k)  == "2.0"         # will truncate that division

i = 5.0
j = 2
i //= j
assert type(i) is float
assert str(i ) == "2.0"
assert j == 2

i = 12
j = 10
k = i % j               # integer mod
assert i == 12
assert j == 10
assert k ==  2

i = 12
j = 10
i %= j
assert i ==  2
assert j == 10

i = 2
j = 3
k = i ** j              # exponentiation
assert i == 2
assert j == 3
assert k == 8

i = 2
j = 3
i **= j
assert i == 8
assert j == 3

i = 2
j = 3
k = i << j              # bit shift left
assert i ==  2
assert j ==  3
assert k == 16

i = 2
j = 3
i <<= j
assert i == 16
assert j ==  3

i = 10                  # 0000 0000 0000 1010
j = ~i                  # 1111 1111 1111 0101: bit complement
k = ~i + 1              # 1111 1111 1111 0110
assert i ==  10
assert j == -11
assert k == -10         # bit complement (flip every bit) then add one is equivelant to negation

i = 10                  # 1010
j = 12                  # 1100
k = i & j               # 1000: bit and
assert i == 10
assert j == 12
assert k ==  8

i = 10
j = 12
i &= j                  # i = i & j
assert i ==  8
assert j == 12          # j is not modified

i = 10                  # 1010
j = 12                  # 1100
k = i | j               # 1110: bit or
assert i == 10
assert j == 12
assert k == 14

i = 10
j = 12
i |= j
assert i == 14
assert j == 12

i = 10                  # 1010
j = 12                  # 1100
k = i ^ j               # 0110: bit exclusive or
assert i == 10
assert j == 12
assert k ==  6

i = 10
j = 12
i ^= j
assert i ==  6
assert j == 12

i = 10                  # 1010
j = 12                  # 1100
i ^= j
assert i ==  6          # 0110
assert j == 12          # 1100
j ^= i
assert i ==  6          # 0110
assert j == 10          # 1010
i ^= j
assert i == 12          # 1100
assert j == 10          # 1010  trick to swap variable values without a temperory

i = 10
j = 12
i += j
assert i == 22
assert j == 12
j = i - j
assert i == 22
assert j == 10
i -= j
assert i == 12
assert j == 10              # same trick with arithmetic, just not as pretty

i = 3
j = 5
k = 7
l = 8
assert (i < j) and (j < k) and (k < l)
assert i < j < k < l        # short hand for the above statement. wouldn't work with other langauges, i < j would be evaluated to a boolean, then it'd be boolean < k, which wouldn't make sense. can also do things like i < j > i == i

a = True
b = True
c = False
assert a and b
assert not (a and c)
assert a or b
assert a or c
assert a and b
assert not (a and c)        # logical and's, or's, not's are in english in python

a = [2, 3, 4]
assert a[1] == 3            # list index...takes 2 args, the list and the index. used like an R-value here
a[1] += 1                   # can use the result of that operator as an L-value. if we couldn't, it'd be kind of useless, to be able to index an array and not be able to modify the element of the array at that spot
assert a[1] == 4

assert [2, 3, 4][1] == 3    # python does not demand an L-value as an arg. no point in doing this. built a list on the fly making it an R-value, modify one of its elements, for no possible point

a = (2, 3, 4)
assert a[1] == 3            # tuple index...can only use the result of the index as an R-value. cannot modify it bc tuples are immutable.
#a[1] += 1                  # TypeError: 'tuple' object does not support item assignment


s = "a"
t = "bc"
u = s + t                   # string concatenation
assert u is not "abc"
assert u ==     "abc"

a = [2]
b = [3, 4]
c = a + b                   # list concatenation...operators are clearly overloaded in python. when we build our own classes we can build our own operators.
assert c is not [2, 3, 4]
assert c ==     [2, 3, 4]
assert c !=     (2, 3, 4)   # tuples and lists NEVER equate

a = (2,)
b = (3, 4)
c = a + b                   # tuple concatenation
assert c is not (2, 3, 4)
assert c ==     (2, 3, 4)
assert c !=     [2, 3, 4]

s = "abc"
t = 2 * s                   # string replication
assert t is not "abcabc"
assert t ==     "abcabc"

a = [2, 3, 4]
b = 2 * a                          # list replication
assert b is not [2, 3, 4, 2, 3, 4]
assert b ==     [2, 3, 4, 2, 3, 4]

a = (2, 3, 4)
b = 2 * a                          # tuple replication
assert b is not (2, 3, 4, 2, 3, 4)
assert b ==     (2, 3, 4, 2, 3, 4)

print("Done.")


"""
we'll be able to overloaded operators for classes we build. we're not able to define brand new operators, we are unable to redefine operators on existing types, and we cannot define operators on existing types that they are undefined by that operator. we only get to invent operators when we are clear that what we are doing is inventing operators which are old tokens on new types. 

tldr: we can only invent operators that are old tokens on new types
"""
