#!/usr/bin/env python3

# -------------------
# FunctionDefaults.py
# -------------------

print("FunctionDefaults.py")

def f (x, y, z = 4) :           # assigning default value for z. constraint: must articulate all non-defaulted args before articulating defaulted args. in other words, the defaulted values must be the "trailing" set.
    return [x, y, z]

#f()                            # TypeError: f() missing 2 required positional args: 'x' and 'y'...not enough args. for it to work you would have to assign defaults for x and y.
#f(2)                           # TypeError: f() missing 1 required positional arg: 'y'...again, not enough args. for it to work you would have to assign a default for y.
assert f(2, 3)    == [2, 3, 4]  # invokes default value
assert f(2, 3, 5) == [2, 3, 5]  # ignores default value



#def g (x, y = 3, z) : # SyntaxError: non-default arg follows default arg...default args must come last
#    return [x, y, z]

def g (x = 2, y = 3, z = 4) :       # default all args
    return [x, y, z]

assert g()         == [2, 3, 4]
assert g(5)        == [5, 3, 4]
assert g(5, 6)     == [5, 6, 4]
assert g(5, 6, 7)  == [5, 6, 7]
assert g(5, z = 7) == [5, 3, 7]     # x is bound to first arg by-position, y is bound to default value, z is bound to 2nd arg by-name
#g(5, x = 6)                        # TypeError: g() got multiple values for keyword arg 'x'...x is already given a value by-position. so cannot define it again by-name.



def h1 (x = []) :                   # defining a function h1 with a MUTABLE default...dangerous.
    x += [2]
    return x

assert h1()    == [2]
assert h1()    == [2, 2]            # python remembers the default
assert h1([1]) == [1, 2]            # normal
assert h1()    == [2, 2, 2]         # it has not forgotten...
assert h1([1]) == [1, 2]            # normal
                                    # this is similar to when we built generators on top of mutables. when we built something lazy like map or zip or a generator, we realize that if we weren't careful and we had modified the thing that we had built the map/zip/generator on top of, then when we actually ran next on the generator, we would see the actual impact of having changed it. the same thing is happening here. BOTTOM LINE: avoid defaulting args to mutable objects.


def h2 (x = ()) :                   # immutable default, now it all works perfectly, but we don't have a list anymore
    x += (2,)
    return x

assert h2()     == (2,)
assert h2()     == (2,)
assert h2((1,)) == (1, 2)
assert h2()     == (2,)
assert h2((1,)) == (1, 2)



def h3 (x = None) :                 # special value in python called None, like Java's Null, clearly an immutable value
    if x is None :                  # checks to see if someone calls the function with no args or calls it explicitly with None, doesn't matter, and then goes and builds a brand new list. so if you must have a mutable arg for you to get what you want, this is the way to default it.
        x = []
    x += [2]
    return x

assert h3()    == [2]
assert h3()    == [2]
assert h3([1]) == [1, 2]
assert h3()    == [2]
assert h3([1]) == [1, 2]

print("Done.")


"""
non-defaulted args come BEFORE defaulted args
do not default args with mutable objects, instead use a mutable object or None
"""