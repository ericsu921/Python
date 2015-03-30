#!/usr/bin/env python3

# ---------
# Reduce.py
# ---------

# https://docs.python.org/3.4/library/functools.html

from functools import reduce
from operator  import add, mul, sub
from unittest  import main, TestCase

def reduce_for_range (bf, a, v) :           # bf will use as its first value the seed, which will be the binary function's first arg and the first elem of the iterable, a[0] will be the binary function's second arg. the second time we call the binary function, we are going to give the it the result of the previous call to the binary function as the first arg, and for the second arg, we'll give it the next item in the iterable, a[1].
    for i in range(len(a)) :                # we are iterating over the indices of the objects and not the objects themselves.
        v = bf(v, a[i])                     # we then use the indices to index the object
    return v

def reduce_while (bf, a, v) :
    p = iter(a)                             # creating an iterator over a, in Java you would call iterator() which turns an Iterator object. this is what is actually happening when you run this line: p = a.__iter__()
    try :
        while True :
            w = next(p)                     # in Java you would do while (hasNext(p)) { w = next(p) }, python doesn't have the hasNext function. python instead wants to exhaust the iterator by calling next one too many times, and in response to being exhausted, call a StopIteration exception, and then do nothing, and just leave
            v = bf(v, w)
    except StopIteration :
        pass
    return v

def reduce_for (bf, a, v) :
    for w in a :                            # a for-in loop does the above function under the hood
        v = bf(v, w)
    return v

def bind (f) :
    class MyUnitTests (TestCase) :
        def test_1 (self) :
            assert f(add, [],                  0)  == 0

        def test_2 (self) :
            assert f(add, [2, 3, 4],           0)  ==  9

        def test_3 (self) :
            assert f(sub, [2, 3, 4],           0)  == -9

        def test_4 (self) :
            assert f(mul, [2, 3, 4],           1)  == 24

        def test_5 (self) :
            assert f(add, ([2, 3, 4], [5, 6]), []) == [2, 3, 4, 5, 6]

        def test_6 (self) :
            assert f(add, [(2, 3, 4), (5, 6)], ()) == (2, 3, 4, 5, 6)

        def test_7 (self) :
            assert f(add, ("abc",     "de"),   "") == "abcde"

    return MyUnitTests

reduce_for_range_tests = bind(reduce_for_range)
reduce_while_tests     = bind(reduce_while)
reduce_for_tests       = bind(reduce_for)

if __name__ == "__main__" :
    main()
