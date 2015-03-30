#!/usr/bin/env python3

# ------------
# Variables.py
# ------------

print("Variables.py")

i = 2
v = i
assert i is v
v += 1
assert i == 2
assert v == 3

a = [2, 3, 4]
b = a
assert a is b
b[1] += 1
assert a[1] == 4
assert a is b

a = (2, 3, 4)
b = a
assert a is b
#b[1] += 1    				# TypeError: 'tuple' object does not support item assignment

a = [2, 3, 4]
b = a[:]					# creates a copy of a and assigns it to b
assert a is not b
assert a ==     b
b[1] += 1
assert a[1] == 3
assert b[1] == 4

a = (2, 3, 4)
b = a[:]
assert a is b   			# tuples are not copiable because they are immutable, can't change it, why do you need a copy?

a = [2, 3, 4]
b = a
assert a is b
b += [5]                    # we are not changeing b itself (the reference), we are changing the list b is pointing to
assert a == [2, 3, 4, 5]    # a is changed too
assert a is b

a = [2, 3, 4]
b = a
assert a is b               # both are point to same list object
b = b + [5]                 # here, we are changing b itself (the reference). b is pointing to a brand new list. b += [5] is not the same as b = b + 5 for lists.
assert a == [2, 3, 4]
assert b == [2, 3, 4, 5]    # python built a brand new list and assigned it to b

a = [2, 3, 4]
b = a
assert a is b
b += (5,)                   # the right hand side does not have to be a list, as long as its an iterable
assert a == [2, 3, 4, 5]
assert a is b

a = [2, 3, 4]
b = a
assert a is b
#b = b + (5,)  				# TypeError: can only concatenate list (not "tuple") to list... when you do a +, list is less tolerant, the right hand side better be a list

a = (2, 3, 4)
b = a
assert a is b
b += (5,)                   # changing b itself, not what b is pointing to (it cannot change what b is point to since it's immutable)
assert a == (2, 3, 4)       # hasn't changed
assert b == (2, 3, 4, 5)    # brand new tuple

a = (2, 3, 4)
b = a
assert a is b
b = b + (5,)                # same as above, changing b itself, for immutables, it ALWAYS changes the reference by building a brand new object and changing the reference to point at it
assert a == (2, 3, 4)
assert b == (2, 3, 4, 5)

a = (2, 3, 4)
b = a
assert a is b
try :
    b += [5]                # python didn't like this, both += and + are intolerant and demand that the right hand side be another tuple. in the world of lists (or mutables for that matter), the += doesn't really do the same thing as +, the += was tolerant of iterables the + was only tolerates only lists. in the world of tuples (or immutables), += is the same and + and both are intolerant, they both must be tuples.
    assert False
except TypeError as e :
    assert len(e.args) == 1
    assert e.args      == ('can only concatenate tuple (not "list") to tuple',)

a = (2, 3, 4)
b = a
assert a is b
#b = b + [5]   # TypeError: can only concatenate tuple (not "list") to tuple

print("Done.")
