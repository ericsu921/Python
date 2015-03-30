#!/usr/bin/env python3

# ---------------
# FunctionDict.py
# ---------------

print("FunctionDict.py")

def f (x, y, **z) :					# z is always going to be a dict
    assert type(z) is dict
    return [x, y, z]

assert f(2, 3)               == [2, 3, {}]
assert f(2, 3, a = 4)        == [2, 3, {'a' : 4}]			# here we give f() an arg by-name that f() has never heard of. as long as we did this after handling all required args, z collects however many of these key-value pairs as we want to give it
assert f(2, 3, a = 4, b = 5) == [2, 3, {'a' : 4, 'b' : 5}]
assert f(2, 3, a = 4, b = 5) == [2, 3, {'b' : 5, 'a' : 4}]	# and of course, order doesn't matter

#f(2, 3, {'b' : 5, 'a' : 4})   # TypeError: f() takes exactly 2 arguments (3 given)...it only accepts name = value, name = value, etc. will not take a dict or an iterable as an arg. in order to feed it a dictionary, you need to unpack it using ** as shown on line 25.
#f(2, 3, [('b', 5), ('a', 4)]) # TypeError: f() takes exactly 2 arguments (3 given)

d = {"b" : 4, "a" : 3}				# keys names are unrelated to params names in f()
u = (2,)
assert d                 == {'b' : 4, 'a' : 3}
assert d                 == {'a' : 3, 'b' : 4}
assert f(2, 5,     **d)  == [2, 5, {'a' : 3, 'b' : 4}]		# unpack the dict with keys that the function has never heard of, which is okay, and the function repacks them
assert f(2, y = 5, **d)  == [2, 5, {'a' : 3, 'b' : 4}]
assert f(y = 5, *u, **d) == [2, 5, {'a' : 3, 'b' : 4}]
assert f(*u, y = 5, **d) == [2, 5, {'a' : 3, 'b' : 4}]
#f(2, **d, y = 5)                                      # SyntaxError: invalid syntax...you must unpack the dictionary LAST

d = {"y" : 3, "x" : 2}
#f(2, **d)                   # TypeError: f() got multiple values for keyword argument 'x'
assert f(**d) == [2, 3, {}]

d = {"y" : 3}
assert f(2,     **d) == [2, 3, {}]
assert f(x = 2, **d) == [2, 3, {}]
#f(**d)                            # TypeError: f() takes exactly 2 arguments (1 given)

d = {"y" : 3, "a" : 2}						# mixture of arbitrary args and args that match param names from the function
assert f(2,     **d) == [2, 3, {'a' : 2}]	# x by-pos, y came from the dict, but there's still more stuff left from the dict, and the function collects that for me
assert f(x = 2, **d) == [2, 3, {'a' : 2}]
#f(**d)                                   	# TypeError: f() takes exactly 2 arguments (1 given)...no x value given

print("Done.")
