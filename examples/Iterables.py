#!/usr/bin/env python3

# ------------
# Iterables.py
# ------------

from itertools import count

def test_iterator (p) :
    assert hasattr(p, "__next__")
    assert hasattr(p, "__iter__")
    q = iter(p)                     # q = p.__iter__()
    assert p is q

    assert next(p) == 2             # p.__next__()
    assert next(p) == 3
    assert next(p) == 4

    try :
        assert next(p) == 5         # p.__next__()
        assert False
    except StopIteration :
        pass

def test_iterable (x) :
    assert not hasattr(x, "__next__")
    assert     hasattr(x, "__iter__")
    p = iter(x)                             # p = x.__iter__()
    assert p is not x
    test_iterator(p)

print("Iterables.py")
                                                        # BELOW ARE ITERATORS:
test_iterator(iter([2, 3, 4]))                          # iter(list)
test_iterator(iter((2, 3, 4)))                          # iter(tuple)
test_iterator(iter({2, 3, 4}))                          # iter(set)
test_iterator(iter({2 : "abc", 3 : "def", 4 : "ghi"}))  # iter(dict)
test_iterator(iter([v for v in [2, 3, 4]]))             # iter(list comprehension)
test_iterator(iter(range(2, 5)))                        # iter(range)
test_iterator(((v for v in [2, 3, 4])))                 # generator
test_iterator(   map(lambda v : v,    [2, 3, 4]))       # map
test_iterator(filter(lambda v : True, [2, 3, 4]))       # filter
                                                        # BELOW ARE ITERABLES:
test_iterable([2, 3, 4])                                # list
test_iterable((2, 3, 4))                                # tuple
test_iterable({2, 3, 4})                                # set
test_iterable({2 : "abc", 3 : "def", 4 : "ghi"})        # dict
test_iterable([v for v in [2, 3, 4]])                   # list comprehension
test_iterable(range(2, 5))                              # range

print("Done.")
