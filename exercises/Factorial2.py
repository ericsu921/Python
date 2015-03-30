#!/usr/bin/env python3

# ------------
# Factorial.py
# ------------

# https://docs.python.org/3.4/library/math.html

from functools import reduce
from math      import factorial
from operator  import mul
from sys       import version
from timeit    import timeit

# recursive procedure - the function calls itself. different from determining if its a recursive process or not. in this case it is a recursive process.
# linear recursive process - we have to wait for recursive calls to come back and then do the multiply. and because its a recursive process, that implies that we have to build a series of stack frames to hold on to compute that recursive call and those stack frames are waiting to do those multiplies. so when the recursion finally bottoms out, all the multiplies happen on the way back up to the top. that implies that we need a bunch of stack space. if we want to compute the factorial of 1000, we need 1000 stack frames.
def factorial_recursion (n) :
    assert n >= 0
    if n < 2 :
        return 1
    return n * factorial_recursion(n - 1)

# recursive procedure
# linear iterative process
def factorial_tail_recursion (n) :
    assert n >= 0
    def f (n, v) :                  # python allows us to build a function within a function. no benefit in doing it in this case but if no one else is interested in this function other than the outer function, its kind of a nice scoping thing to do so that the name doesn't collide with other functions outside of this scope.
        assert n >= 0
        assert v >= 1
        if n < 2 :
            return v
        return f(n - 1 , n * v)     # in the previous function, we are waiting for the recursive call to come back to then do the multiply. on this line, we're not waiting for anything. so what a compiler could do is turn this kind of recursion, which is called tail recursion, into iteration, a loop, and it won't need a bunch of stack frames. some languages will do it automatically, some won't. python won't, so this is a moronic thing to do in python because it is clearly an iterative problem, and you're moronically consuming an incredible amount of stack frames to do it. no one uses tail recursion in python bc it's inefficient. although it is in some sense elegant, it is also performance horrible.
    return f(n, 1)

# iterative procedure
# linear iterative process
def factorial_while (n) :
    assert n >= 0
    v = 1
    while n > 1 :
        v *= n
        n -= 1
    return v

def factorial_range_for (n) :
    assert n >= 0
    v = 1
    for i in range(1, n + 1) :          # in python2, it builds an actual list under the hood and iterates through that list. in python3, it returns a generator, which is an iterable that spits out the numbers one at a time. python2 has a function called xrange(), which is the generator version of range, but in python3, they decided to replace range() with xrange() in terms of functionality, and call it range()
        v *= i
    return v

def factorial_range_reduce (n) :
    assert n >= 0
    return reduce(mul, range(1, n + 1), 1)          # 1st arg takes a binary function, 2nd arg is an iterable, 3rd arg is the seed, the number reduce starts with. reduce will invoke whatever operator we say between all the elements in the iterable starting with the seed being all the way on the left. to compute factorial using reduce, the seed must be the multiplicative identity, which is 1. if we wanted to use reduce with add, we would be interested in the sum, and the seed would then be the additive identity, which is 0.

def test (f) :
    print(f.__name__)
    assert f(0) ==   1
    assert f(1) ==   1
    assert f(2) ==   2
    assert f(3) ==   6
    assert f(4) ==  24
    assert f(5) == 120
    t = timeit(f.__name__ + "(100)", "from __main__ import " + f.__name__, number = 1000)       # we are telling it to do factorial of 100, 1000 times and time it
    print("{:.2f} milliseconds".format(t * 1000))
    print()

print("Factorial.py")
print()

print(version)
print()

test(factorial_recursion)
test(factorial_tail_recursion)
test(factorial_while)
test(factorial_range_for)
test(factorial_range_reduce)
test(factorial)

print("Done.")

"""
Factorial.py

3.4.2 (v3.4.2:ab2c023a9432, Oct  5 2014, 20:42:22)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)]

factorial_recursion
19.50 milliseconds

factorial_tail_recursion
25.03 milliseconds

factorial_while
12.65 milliseconds

factorial_range_for
7.63 milliseconds

factorial_range_reduce
7.67 milliseconds

factorial
1.12 milliseconds

Done.
"""
