#!/usr/bin/env python3

# --------------------
# FunctionUnpacking.py
# --------------------

import collections

print("FunctionUnpacking.py")

def f (x, y, z) :
    return [x, y, z]

t = (3, 4)                              # tuple
assert t            == (3, 4)
assert t            != (4, 3)           # order matters
assert f(2, t, 5)   == [2, (3, 4), 5]   # passed the tuple as the 2nd arg
assert f(2, 5, t)   == [2, 5, (3, 4)]   # 3rd arg
assert f(2, *t)     == [2, 3, 4]        # unpacking t. all star demands is that the thing be iterable, and when you unpack, it better have the right number of items given what you have already provided in some other way
assert f(z = 2, *t) == [3, 4, 2]        # when we unpack the tuple, it is no longer bound to y and z, but is now bound to x and y
assert f(*t, z = 2) == [3, 4, 2]        # order of pass-by-name and unpacking doesn't matter (when you specify it arguments, but order does matter when the passing takes place, the arg passed by-name must be a trailing set of the params). also, you cannot unpack more than once.
#f(*t, 2)                               # SyntaxError: invalid syntax...pass-by-position ALWAYS comes first. order definitely matter here.
#f(x = 2, *t)                           # f() got multiple values for arg 'x'...order doesn't matter here. but when we unpack, python iterates through t and effectively passes the values of t by-position, and these values must come before values assigned by-name. this explains why you cannot unpack more than once, bc then you will be assigning multiple values to the elements assigned by the first unpacking. the priority is by-position, by-unpacking, then by-name. so when we're finished with passing-by-position, that's when we start invoking the iterable-unpacking.
#f(*t)                                  # TypeError: f() takes exactly 3 args (2 given)...no enough info
#f(2, 5, *t)                            # TypeError: f() takes exactly 3 args (4 given)...too much info

l = [3, 4]
assert l            == [3, 4]
assert l            != [4, 3]           # order matters
assert f(2, l, 5)   == [2, [3, 4], 5]
assert f(2, 5, l)   == [2, 5, [3, 4]]
assert f(2, *l)     == [2, 3, 4]
assert f(z = 2, *l) == [3, 4, 2]
assert f(*l, z = 2) == [3, 4, 2]
#f(*l, 2)                              # SyntaxError: only named args may follow *expression
#f(x = 2, *l)                          # f() got multiple values for arg 'x'
#f(*l)                                 # TypeError: f() takes exactly 3 args (2 given)
#f(2, 5, *l)                           # TypeError: f() takes exactly 3 args (4 given)

s = {3, 4}
assert s                 == {3, 4}          # order does NOT matter
assert s                 == {4, 3}
assert f(2, s, 5)        == [2, {3, 4}, 5]
assert f(2, 5, s)        == [2, 5, {3, 4}]
assert set(f(2, *s))     == {2, 3, 4}       # cannot predict order so we must cast the output of f() to a set and compare it to another set, only comparing the content
assert set(f(z = 2, *s)) == {2, 3, 4}
assert set(f(*s, z = 2)) == {2, 3, 4}
#f(*s, 2)                                   # SyntaxError: only named args may follow *expression
#f(x = 2, *s)                               # f() got multiple values for arg 'x'
#f(*s)                                      # TypeError: f() takes exactly 3 args (2 given)
#f(2, 5, *s)                                # TypeError: f() takes exactly 3 args (4 given)

d = {"b" : 4, "a" : 3}
assert type(d.keys()) is not collections.KeysView       # the results of .keys() is not a simple lists. it returns another one of these exotic generators that spit out the keys one at a time.
assert isinstance(d.keys(), collections.KeysView)
assert set(d.keys()) == {"a", "b"}

assert type(d.values()) is not collections.ValuesView   # generator
assert isinstance(d.values(), collections.ValuesView)
assert set(d.values()) == {3, 4}

assert type(d.items()) is not collections.ItemsView     # generator
assert isinstance(d.items(), collections.ItemsView)
assert set(d.items()) == {("a", 3), ("b", 4)}

assert d                      == {'b' : 4, 'a' : 3}
assert d                      == {'a' : 3, 'b' : 4}             # order doesn't matter
assert f(2, d, 5)             == [2, {'a' : 3, 'b' : 4}, 5]     # passing as 2nd arg
assert f(2, 5, d)             == [2, 5, {'a' : 3, 'b' : 4}]     # 3rd arg
assert set(f(2, *d.keys()))   == {2, 'a', 'b'}                  # unpack keys
assert set(f(2, *d.values())) == {2, 3, 4}                      # unpack values
assert set(f(2, *d.items()))  == {2, ('a', 3), ('b', 4)}        # unpack key/value pairs
assert set(f(2, *d))          == {2, 'a', 'b'}                  # *d returns keys
assert set(f(z = 2, *d))      == {2, 'a', 'b'}
assert set(f(*d, z = 2))      == {2, 'a', 'b'}
#f(*d, 2)                                                       # SyntaxError: only named args may follow *expression
#f(x = 2, *d)                                                   # f() got multiple values for arg 'x'
#f(*d)                                                          # TypeError: f() missing 1 required positional arg: 'z'
#f(2, 5, *d)                                                    # TypeError: f() takes 3 positional args but 4 were given
#f(2, **d)                                                      # TypeError: f() got an unexpected keyword arg 'a'

d = {"z" : 4, "y" : 3, "x" : 2}                                 # IMPORTANT: the keys MUST match the param names of the function
#f(2, **d)                                                      # TypeError: f() got multiple values for keyword arg 'x'...too many values for x, we are assigning a value to x by position and by dict-unpacking, no good.
assert f(**d) == [2, 3, 4]                                      # dictionary unpacking, * requires an iterable, ** requires a dict of which the keys must perfectly match the params names of the function, and the total number of args passed into the function must match the number of params in that function

d = {"z" : 4, "y" : 3}              # matches 2 names of the params of function f
assert f(2,     **d) == [2, 3, 4]   # x is passed-by-position with the value 2, the rest is unpack
assert f(x = 2, **d) == [2, 3, 4]   # same story but this time passed-by-name
#f(**d, 2)                          # SyntaxError: invalid syntax...pass-by-pos ALWAYS comes first, dict-unpacking ALWAYS comes last
#f(**d, x = 2)                      # SyntaxError: invalid syntax
#f(**d)                             # TypeError: f() takes exactly 3 args (2 given)
#f(2, 5, **d)                       # TypeError: f() got multiple values for keyword arg 'y'

d = {"y" : 3}
#f(2, 4, **d)                       # TypeError: f() got multiple values for arg 'y'...already gave y a value
assert f(2, z = 4, **d) == [2, 3, 4]

d = {"z" : 4, "y" : 3, "t" : 5}     # keys don't match function f()'s param names. param names MUST match for this to work.
#f(2,     **d)                      # TypeError: f() got an unexpected keyword arg 't'
#f(x = 2, **d)                      # TypeError: f() got an unexpected keyword arg 't'
#f(**d)                             # TypeError: f() got an unexpected keyword arg 't'

t = (2, 3)
d = {"z" : 4}
assert f(*t, **d) == [2, 3, 4]
#f(**d, *t)                         # SyntaxError: invalid syntax...again, dict-unpacking MUST come last. iterable unpacking can be either before or after pass-by-name. pass-by-position MUST come first.

print("Done.")

"""
dictionary unpacking is reflective. it looks at the strings of the keys during runtime and compares them to the string names of the args. it has to remember those param names. it's fragile. but even pass-by-name is fragile. pass-by-name a thousand times. the moment you change the param name, all the calls break.


pass-by-position:   first (always)
pass-by-name:       after pass-by-position, before dict-unpacking
iterable unpacking  after pass-by-position, before dict-unpacking
dict-unpacking      last (always)

but when you actually pass the values and unpack, it does it in this order (by-value, iterable-unpacking, by-name, dict-unpacking)
"""
