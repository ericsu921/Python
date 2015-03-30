#!/usr/bin/env python3

# -------
# Map2.py
# -------

# https://docs.python.org/3.4/library/functions.html#map

from unittest import main, TestCase

def map_for_range (uf, a) :                     # demands that the thing be indexable, iterates over the indices and then uses a[i] to get the value, calls iter() on that value, and then calls yield. because there is yield, when we call map, that returns to the caller a map object which acts like a generator that we can then call next on and iterate over and at each call to next, the function yield a value
    for i in range(len(a)) :
        yield uf(a[i])

def map_while (uf, a) :
    p = iter(a)
    try :
        while True :
            yield uf(next(p))
    except StopIteration :
        pass

def map_for (uf, a) :                           # demands that a be iterable
    for v in a :
        yield uf(v)

def map_generator (uf, a) :
    return (uf(v) for v in a)

def bind (f) :
    class MyUnitTests (TestCase) :
        def test_1 (self) :
            a = ()
            assert list(f(lambda x : x ** 2, a)) == []

        def test_2 (self) :
            a = (2, 3, 4)
            assert list(f(lambda x : x ** 2, a)) == [4,  9, 16]

        def test_3 (self) :
            a = ([2], [3], [4])
            assert list(f(lambda x : x + [5], a)) == [[2, 5], [3, 5], [4, 5]]

        def test_4 (self) :
            a = ("abc", "def", "ghi")
            assert list(f(lambda x : x + "xyz", a)) == ["abcxyz", "defxyz", "ghixyz"]

    return MyUnitTests

map_for_range_tests = bind(map_for_range)
map_while_tests     = bind(map_while)
map_for_tests       = bind(map_for)
map_generator_tests = bind(map_generator)

if __name__ == "__main__" :
    main()
