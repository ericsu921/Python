#!/usr/bin/env python3

# ------
# Map.py
# ------

# https://docs.python.org/3.4/library/functions.html#map

from unittest import main, TestCase

def map (uf, a) :
    ...

class MyUnitTests (TestCase) :
    def test_1 (self) :
        a = ()
        assert list(map(lambda x : x ** 2, a)) == []                            # the map produces a generator, and we fed map to list's constructor, which wants an iterable as an arg, which it will then consume and make the elems of the container. we fed it to the list so that we can show the elems in the form of a list.

    def test_2 (self) :
        a = (2, 3, 4)
        assert list(map(lambda x : x ** 2, a)) == [4,  9, 16]

    def test_3 (self) :
        a = ([2], [3], [4])
        assert list(map(lambda x : x + [5], a)) == [[2, 5], [3, 5], [4, 5]]

    def test_4 (self) :
        a = ("abc", "def", "ghi")
        assert list(map(lambda x : x + "xyz", a)) == ["abcxyz", "defxyz", "ghixyz"]

if __name__ == "__main__" :
    main()
