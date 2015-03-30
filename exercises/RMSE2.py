#!/usr/bin/env python3

# --------
# RMSE2.py
# --------
from functools import reduce
from math      import sqrt
from numpy     import mean, sqrt, square, subtract
from sys       import version
from timeit    import timeit

def rmse_while (a, p) :
    """
    O(1) in space
    O(n) in time
    """
    assert hasattr(a, "__len__")            # we are calling functions on these objects (e.g. lists, tuples, etc.) and what gives us the right to call a certain set of functions is whether that object that we're trying to call the function on has an attribute that can support that function. in order to call the len() function on this object, it must have then __len__ attribute.
    assert hasattr(p, "__len__")
    assert hasattr(a, "__getitem__")        # indexable
    assert hasattr(p, "__getitem__")
    i = 0
    v = 0
    while i != len(a) :                     # this is a bad idea because this algorithm is insisting on something that it has no reason to insist on. it is insisting that a and p be indexable and there is no reason they need to be indexable in order to solve this problem. all they need to do is start from the beginning, march through the items without skipping, all the way to the end. we don't need to randomly access items. if we were doing quicksort, it would need to be indexable. it must be iterable.
        v += (a[i] - p[i]) ** 2
        i += 1
    return sqrt(v / len(a))

def rmse_range_for (a, p) :
    """
    O(1) in space
    O(n) in time
    """
    assert hasattr(a, "__len__")
    assert hasattr(p, "__len__")
    assert hasattr(a, "__getitem__")
    assert hasattr(p, "__getitem__")
    v = 0
    for i in range(len(a)) :            # python doesn't have the classic for-loop that you find in Java. the ability for me to do for i in anything is that that anything be iterable. that's the definition of being iterable, that I can do a for i in it.
        v += (a[i] - p[i]) ** 2         # still demands that a and p be indexable, which is a stronger thing than i need them to be
    return sqrt(v / len(a))

def rmse_zip_for (a, p) :
    """
    O(1) in space
    O(n) in time
    """
    assert hasattr(a, "__len__")
    assert hasattr(p, "__len__")
    assert hasattr(a, "__iter__")       # must have the iter attribute, which means it must be able to have iter() called on it, which unsurprisingly means it must be iterable
    assert hasattr(p, "__iter__")
    z = zip(a, p)
    v = 0
    for x, y in z :                     # iterating through 2 items at a time. z must be an iterable of iterables, and in this case, of exactly length two. 
        v += (x - y) ** 2
    return sqrt(v / len(a))

def rmse_zip_reduce (a, p) :
    """
    O(1) in space
    O(n) in time
    """
    assert hasattr(a, "__len__")
    assert hasattr(p, "__len__")
    assert hasattr(a, "__iter__")
    assert hasattr(p, "__iter__")
    z = zip(a, p)
    v = reduce(lambda x, a : x + (a[0] - a[1]) ** 2, z, 0)      # reduce is a higher order function that wants for an arg a binary function. reduce produce the sum of the squares of the differences. this function is now amenable to something that's iterable but not indexable. we could give this function two sets, and it would still work.
    return sqrt(v / len(a))

def rmse_map_sum (a, p) :
    """
    O(1) in space
    O(n) in time
    """
    assert hasattr(a, "__len__")
    assert hasattr(p, "__len__")
    assert hasattr(a, "__iter__")
    assert hasattr(p, "__iter__")
    v = sum(map(lambda x, y : (x - y) ** 2, a, p))              # map takes in the binary function and it produces an iterable over these squares of differences. we then sum it using sum(). we could have added them up using reduce(), but there is no need to do that. note that this does NOT produce another container of any sort. if we ran this on two million element lists, all we do create a generator that lazily spits out the elems one at a time.
    return sqrt(v / len(a))

def rmse_zip_list_sum (a, p) :
    """
    O(n) in space
    O(n) in time
    """
    assert hasattr(a, "__len__")
    assert hasattr(p, "__len__")
    assert hasattr(a, "__iter__")
    assert hasattr(p, "__iter__")
    z = zip(a, p)
    v = sum([(x - y) ** 2 for x, y in z])               # [...] list comprehension. you can write code inside the square brackets to produce the elems that you want to be inside the list. the syntax for the code is similar to the for in machinery, but just a bit backwards. [<expression body> <for-in>]. [sq_diff for in x, y in z] wouldn't work! you don't need the name of the function, you need the body, or just an expression. note that this DOES produce a brand new container with all the elems. if we ran this on two million element lists, we could create a brand new list with a million elements. 
    return sqrt(v / len(a))

def rmse_zip_generator_sum (a, p) :
    """
    O(1) in space
    O(n) in time
    """
    assert hasattr(a, "__len__")
    assert hasattr(p, "__len__")
    assert hasattr(a, "__iter__")
    assert hasattr(p, "__iter__")
    z = zip(a, p)
    v = sum((x - y) ** 2 for x, y in z)     # eliminated the square brackets, which now produces a generator instead of a list. no extra parentheses needed. only needed when standing alone
    return sqrt(v / len(a))

def rmse_numpy (a, p) :
    """
    O(n) in space
    O(n) in time
    """
    return sqrt(mean(square(subtract(a, p))))

def test (f) :
    print(f.__name__)
    assert f((2, 3, 4), (2, 3, 4)) == 0
    assert f((2, 3, 4), (3, 2, 5)) == 1
    assert f((2, 3, 4), (4, 1, 6)) == 2
    assert f((2, 3, 4), (4, 3, 2)) == 1.632993161855452
    t = timeit("assert " + f.__name__ + "(10000 * [1], 10000 * [5]) == 4", "from __main__ import " + f.__name__, number = 100)          # here you effectively build code in the form of strings, which it then evaluates a certain number of times (that's how python does it anyway). grab the assert, grab the name of the function, build a list of 10000 ones and another of 10000 fives, take the rmse and ensure that it == 4. we then did that 100 times and timed it.
    print("{:.2f} milliseconds".format(t * 1000))
    print()

print("RMSE2.py")
print()

print(version)
print()

test(rmse_while)
test(rmse_range_for)
test(rmse_zip_for)
test(rmse_zip_reduce)
test(rmse_map_sum)
test(rmse_zip_list_sum)
test(rmse_zip_generator_sum)
test(rmse_numpy)

print("Done.")

"""
rmse.py

3.4.2 (v3.4.2:ab2c023a9432, Oct  5 2014, 20:42:22)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)]

rmse_while
1393.41 milliseconds

rmse_range_for
1268.21 milliseconds

rmse_zip_for
924.56 milliseconds

rmse_zip_reduce
1246.97 milliseconds

rmse_map_sum
1019.86 milliseconds

rmse_zip_list_sum
891.52 milliseconds

rmse_zip_generator_sum
910.61 milliseconds

rmse_numpy
325.95 milliseconds

Done.
"""
